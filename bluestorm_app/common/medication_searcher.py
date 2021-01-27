from pandas import read_csv

from .word_checker import WordChecker
from settings import DATABASE_FILE_PATH


class MedicationSearcher:
    def __init__(self):

        self.checker = WordChecker()

        self.medications = read_csv(
            DATABASE_FILE_PATH,
            delimiter="~",
            usecols=["Ingredient", "DF;Route", "Trade_Name", "Applicant", "Strength"],
        )

        self.medications = self.medications.astype(
            {
                "Ingredient": str,
                "DF;Route": str,
                "Trade_Name": str,
                "Applicant": str,
                "Strength": str,
            }
        )

    def get_ingredients(self, dictionary):

        results = []

        for ingredient in dictionary["Ingredient"].split("; "):
            results.append({"name": ingredient})

        return results

    def get_dfs(self, dictionary):

        results = []

        for df in dictionary["DF;Route"].split(";")[0].split(","):
            results.append({"method": df})

        return results

    def get_routes(self, dictionary):

        results = []

        for route in dictionary["DF;Route"].split(";")[1].split(","):
            results.append({"method": route})

        return results

    def get_trade_names(self, dictionary):

        results = []

        for trade_name in dictionary["Trade_Name"].split("; "):
            results.append({"name": trade_name})

        return results

    def get_applicants(self, dictionary):

        results = []

        for applicant in dictionary["Applicant"].split("; "):
            results.append({"name": applicant})

        return results

    def get_strengths_and_warnings(self, dictionary):

        strengths = []
        warnings = []

        for strength in dictionary["Strength"].split(";"):

            if " **" in strength:
                strengths.append({"amount": strength.split(" **")[0]})
                warnings.append({"message": strength.split(" **")[1].split("**")[0]})
            else:
                strengths.append({"amount": strength})

        return [strengths, warnings]

    def search(self, word):

        results = []

        word_checked = self.checker.get_correction(word)

        medications = self.medications.loc[
            self.medications["Trade_Name"].str.lower().str.contains(word_checked)
        ]

        for medication in medications.to_dict("records"):

            strengths, warnings = self.get_strengths_and_warnings(medication)

            results.append(
                {
                    "ingredients": self.get_ingredients(medication),
                    "dfs": self.get_dfs(medication),
                    "routes": self.get_routes(medication),
                    "trade_names": self.get_trade_names(medication),
                    "applicants": self.get_applicants(medication),
                    "strengths": strengths,
                    "warning_messages": warnings,
                }
            )

        return results
