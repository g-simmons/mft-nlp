import altair as alt
import pandas as pd
from pathlib import Path


def load_results():
    data = pd.concat(
        [pd.read_csv(str(p), sep="\t") for p in Path("./data/results").glob("*.tsv")]
    )
    return data

def main():
    data = load_results()
    print(data["dataset"].value_counts())
    print(data["method"].value_counts())

    for dataset, group in data.groupby("dataset"):
        print(dataset)
        input_dropdown = alt.binding_select(
            options=["F1", "Precision", "Recall"], name="Metric"
        )
        selection = alt.selection_single(
            fields=["metric"], bind=input_dropdown, init={"metric": "F1"}
        )
        chart = (
            alt.Chart(data[data.foundation == "Avg"])
            .mark_point()
            .encode(
                x=alt.X(
                    "year",
                    axis=alt.Axis(
                        title="Year",
                        tickMinStep=1,
                        format=".0f",
                    ),
                    scale=alt.Scale(domain=[2000, 2030]),
                ),
                y=alt.Y("value:Q", axis=alt.Axis(title="F1 (Avg)")),
                color=alt.Color("method"),
                tooltip=[
                    "variant",
                    "metric",
                    "foundation",
                    "method",
                    "task",
                    "schema",
                    "std",
                    "value",
                ],
            )
            .add_selection(selection)
            .transform_filter(selection)
            .interactive()
        )
        chart.save(f"./assets/charts/{dataset}.json")

if __name__ == "__main__":
    main()