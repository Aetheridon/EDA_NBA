import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="darkgrid")
plt.style.use("dark_background")
plt.figure(figsize=(10, 6))

dataset = pd.read_csv("all_seasons.csv")

def convert_cm_to_feet(cm):
    t_inches = cm / 2.54
    feet = int(t_inches // 12)
    inches = int(round(t_inches % 12))
    return f"{feet}'{inches}\""


def height_pdf(dataset: pd.DataFrame):
    heights = dataset["player_height"]

    ax = sns.histplot(heights, bins=20, kde=True, stat="density", alpha=0.7, color="cyan", edgecolor="white")

    xticks = ax.get_xticks()
    labels = [convert_cm_to_feet(cm) for cm in xticks]
    ax.set_xticklabels(labels, color="white")

    plt.title("PDF of NBA Player Heights", color="white", fontsize=16)
    plt.xlabel("Height (Feet)", color="white")
    plt.ylabel("Probability Density", color="white")
    plt.xticks(color="white")
    plt.yticks(color="white")
    plt.grid(True, color="#444444")
    plt.tight_layout()
    plt.savefig("pdf_heights.png", dpi=300, facecolor="black")


def weight_pdf(dataset: pd.DataFrame):
    weights = dataset["player_weight"]
    
    sns.histplot(weights, bins=20, kde=True, stat="density", alpha=0.7, color="cyan", edgecolor="white")
    plt.title("PDF of NBA Player Weights", color="white", fontsize=16)
    plt.xlabel("Weight (KG)", color="white")
    plt.ylabel("Probability Density", color="white")
    plt.xticks(color="white")
    plt.yticks(color="white")
    plt.grid(True, color="#444444")
    plt.tight_layout()
    plt.savefig("pdf_weights.png", dpi=300, facecolor="black")


def pts_to_height(dataset: pd.DataFrame):
    bins = np.arange(170, 221, 5)
    labels = [f"{b}-{b+4}" for b in bins[:-1]]
    dataset["height_range"] = pd.cut(dataset["player_height"], bins=bins, labels=labels)

    avg_pts_by_height = dataset.groupby("height_range")["pts"].mean().sort_values(ascending=False)

    sns.barplot(x=avg_pts_by_height.index, y=avg_pts_by_height.values, palette="coolwarm")

    plt.title("Average Points per Game by Height", fontsize=16, color="white")
    plt.xlabel("Height", color="white")
    plt.ylabel("Points per Game", color="white")
    plt.xticks(color="white")
    plt.yticks(color="white")
    plt.grid(True, color="#444444")
    plt.tight_layout()
    plt.savefig("avg_points_by_height.png", dpi=300, facecolor="black")

# height_pdf(dataset)
# weight_pdf(dataset)
pts_to_height(dataset)