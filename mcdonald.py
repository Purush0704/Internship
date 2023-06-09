{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 130
        },
        "id": "cfqLAVvUWuMB",
        "outputId": "35fc2584-a3a8-4cf0-d2df-32c23b6c16c7"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-1874173ca7fd>\"\u001b[0;36m, line \u001b[0;32m43\u001b[0m\n\u001b[0;31m    for i, feature in enumerate(['CHEAP', 'EXPENSIVE', 'FATTENING', 'DISGUSTING', '\u001b[0m\n\u001b[0m                                                                                   ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m EOL while scanning string literal\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "mcdonalds = pd.read_csv(\"https://raw.githubusercontent.com/bioinformatics-core-shared-training/MSA-data/main/mcdonalds.csv\")\n",
        "\n",
        "print(mcdonalds.columns)\n",
        "print(mcdonalds.shape)\n",
        "print(mcdonalds.head(3))\n",
        "\n",
        "from sklearn.decomposition import PCA\n",
        "MD_x = (mcdonalds.iloc[:, 0:11] == \"Yes\").astype(int)\n",
        "\n",
        "MD_pca = PCA()\n",
        "MD_pca.fit(MD_x)\n",
        "print(\"Explained variance ratio:\", MD_pca.explained_variance_ratio_)\n",
        "print(\"Cumulative explained variance ratio:\", MD_pca.explained_variance_ratio_.cumsum())\n",
        "print(\"Factor loadings:\\n\", MD_pca.components_)\n",
        "import numpy as np\n",
        "from sklearn.decomposition import PCA\n",
        "\n",
        "# load data into numpy array\n",
        "data = np.array([[0.477, -0.36, 0.30, -0.055, -0.308, 0.17, -0.28, 0.01, -0.572, 0.110, 0.045],\n",
        "                 [0.155, -0.02, 0.06, 0.142, 0.278, -0.35, -0.06, -0.11, 0.018, 0.666, -0.542],\n",
        "                 [0.006, -0.02, 0.04, -0.198, 0.071, -0.36, 0.71, 0.38, -0.400, 0.076, 0.142],\n",
        "                 [-0.116, 0.03, 0.32, 0.354, -0.073, -0.41, -0.39, 0.59, 0.161, 0.005, 0.251],\n",
        "                 [-0.304, 0.06, 0.80, -0.254, 0.361, 0.21, 0.04, -0.14, 0.003, -0.009, 0.002],\n",
        "                 [0.108, 0.09, 0.06, 0.097, 0.108, -0.59, -0.09, -0.63, -0.166, -0.240, 0.339],\n",
        "                 [0.337, 0.61, 0.15, -0.119, -0.129, -0.10, -0.04, 0.14, -0.076, -0.428, -0.489],\n",
        "                 [0.472, -0.31, 0.29, 0.003, -0.211, -0.08, 0.36, -0.07, 0.639, -0.079, 0.020],\n",
        "                 [-0.329, -0.60, -0.02, -0.068, -0.003, -0.26, -0.07, 0.03, -0.067, -0.454, -0.490],\n",
        "                 [0.214, -0.08, -0.19, -0.763, 0.288, -0.18, -0.35, 0.18, 0.186, 0.038, 0.158],\n",
        "                 [-0.375, 0.14, 0.09, -0.370, -0.729, -0.21, -0.03, -0.17, 0.072, 0.290, -0.041]])\n",
        "\n",
        "# perform PCA\n",
        "pca = PCA(n_components=2)\n",
        "projected = pca.fit_transform(data)\n",
        "\n",
        "# plot the projected data\n",
        "import matplotlib.pyplot as plt\n",
        "plt.scatter(projected[:, 0], projected[:, 1], color='grey')\n",
        "\n",
        "# add arrows for the original segmentation variables\n",
        "loadings = pca.components_.T * np.sqrt(pca.explained_variance_)\n",
        "for i, feature in enumerate(['CHEAP', 'EXPENSIVE', 'FATTENING', 'DISGUSTING']\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "from sklearn.cluster import KMeans\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "np.random.seed(1234)\n",
        "\n",
        "# standardize the data\n",
        "scaler = StandardScaler()\n",
        "MD_x_scaled = scaler.fit_transform(MD_x)\n",
        "\n",
        "# define range of clusters to test\n",
        "k_range = range(2, 9)\n",
        "\n",
        "# initialize list to store cluster labels and within-cluster sum of squares\n",
        "cluster_labels = []\n",
        "wcss = []\n",
        "\n",
        "# loop over the range of clusters\n",
        "for k in k_range:\n",
        "    # fit KMeans model and obtain cluster labels and within-cluster sum of squares\n",
        "    kmeans = KMeans(n_clusters=k, n_init=10, random_state=1234)\n",
        "    kmeans.fit(MD_x_scaled)\n",
        "    cluster_labels.append(kmeans.labels_)\n",
        "    wcss.append(kmeans.inertia_)\n",
        "\n",
        "# re-label clusters using stepFlexclust function\n",
        "def relabel_clusters(labels):\n",
        "    unique_labels = np.unique(labels)\n",
        "    relabeled_labels = np.zeros(len(labels))\n",
        "    for i, label in enumerate(unique_labels):\n",
        "        relabeled_labels[labels == label] = i\n",
        "    return relabeled_labels\n",
        "\n",
        "MD_km28 = []\n",
        "for i in range(len(cluster_labels)):\n",
        "    relabeled_labels = relabel_clusters(cluster_labels[i])\n",
        "    MD_km28.append(relabeled_labels)"
      ],
      "metadata": {
        "id": "MpsqEGG9Yrsv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from flexclust import stepFlexclust, relabel\n",
        "MD_k = stepFlexclust(MD.x, range(2,9), nrep=10, verbose=False)\n",
        "MD_k = relabel(MD_k)\n",
        "\n",
        "# plot the clustering results\n",
        "plt.plot(range(2,9), MD_k$size, type=\"b\", xlab=\"number of segments\", ylab=\"size of segments\")\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 321
        },
        "id": "pgLuY4UFciCd",
        "outputId": "e54ee56d-b7a2-43fe-d69b-bb931b06146f"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-43bf646cdc57>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mflexclust\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mstepFlexclust\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrelabel\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'flexclust'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "    # Cluster with k-means\n",
        "    kmeans = KMeans(n_clusters=n_seg[j], n_init=n_rep)\n",
        "    kmeans.fit(X_boot)\n",
        "    labels_boot = kmeans.labels_\n",
        "    \n",
        "    # Compute adjusted Rand index\n",
        "    ari_boot[i, j] = adjusted_rand_score(labels_true=labels_boot, labels_pred=kmeans.labels_)\n"
      ],
      "metadata": {
        "id": "KkARPzYociyp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Assuming MD.km28[[\"4\"]] contains a vector of values\n",
        "values = MD.km28[\"4\"]\n",
        "\n",
        "# Create histogram\n",
        "plt.hist(values, bins=20, range=[0, 1])\n",
        "\n",
        "# Add labels and title\n",
        "plt.xlabel('Value')\n",
        "plt.ylabel('Frequency')\n",
        "plt.title('Histogram of MD.km28[[\"4\"]]')\n",
        "\n",
        "plt.show()\n"
      ],
      "metadata": {
        "id": "VIHPu9Chc3lM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "s\n",
        "from sklearn.metrics import adjusted_rand_score\n",
        "\n",
        "np.random.seed(1234)\n",
        "md_x = np.random.rand(200, 2)\n",
        "\n",
        "# K-means clustering\n",
        "km28 = {}\n",
        "for k in range(2, 9):\n",
        "    km28[str(k)] = KMeans(n_clusters=k, n_init=10).fit(md_x)\n",
        "\n",
        "# Bootstrap K-means clustering\n",
        "b28 = {}\n",
        "for k in range(2, 9):\n",
        "    b28[str(k)] = []\n",
        "    for i in range(100):\n",
        "        idx = np.random.choice(md_x.shape[0], md_x.shape[0], replace=True)\n",
        "        b28[str(k)].append(KMeans(n_clusters=k, n_init=10).fit(md_x[idx]))\n",
        "\n",
        "# Plot global stability boxplot\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "fig, ax = plt.subplots()\n",
        "ax.boxplot([adjusted_rand_score(km28[str(k)].labels_, b28[str(k)][i].labels_)\n",
        "            for k in range(2, 9) for i in range(100)],\n",
        "           positions=np.arange(2, 9))\n",
        "ax.set_xlabel('number of segments')\n",
        "ax.set_ylabel('adjusted Rand index')\n",
        "\n",
        "# Histogram of one segment\n",
        "k4 = km28['4']\n",
        "fig, ax = plt.subplots()\n",
        "ax.hist(md_x[k4.labels_ == 3, 0], bins=10, range=(0, 1))\n",
        "ax.set_xlim(0, 1)\n",
        "ax.set_xlabel('segment variable')\n",
        "ax.set_ylabel('frequency')\n",
        "\n",
        "# Segment level stability within solutions (SLSW)\n",
        "r4 = []\n",
        "for i in range(100):\n",
        "    idx = np.random.choice(md_x.shape[0], md_x.shape[0], replace=True)\n",
        "    r4.append([adjusted_rand_score(k4.labels_, KMeans(n_clusters=4, n_init=10).fit(md_x[idx]).labels_)\n",
        "               for j in range(4)])\n",
        "fig, ax = plt.subplots()\n",
        "ax.plot(np.arange(1, 5), np.mean(r4, axis=0))\n",
        "ax.fill_between(np.arange(1, 5), np.percentile(r4, 5, axis=0), np.percentile(r4, 95, axis=0), alpha=0.3)\n",
        "ax.set_ylim(0, 1)\n",
        "ax.set_xlabel('segment number')\n",
        "ax.set_ylabel('segment stability')\n"
      ],
      "metadata": {
        "id": "VSCicOxndJwg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from mixtools import GMM, stepAIC\n",
        "\n",
        "np.random.seed(1234)\n",
        "\n",
        "# Generate some data\n",
        "MD = np.random.binomial(n=1, p=0.5, size=(100, 28))\n",
        "\n",
        "# Fit a mixture model with 2-8 components\n",
        "fit = stepAIC(MD, maxcomp=8, k=2)\n",
        "\n",
        "# Print the results\n",
        "print(fit.summary())"
      ],
      "metadata": {
        "id": "zD4AFOgodpWZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.mixture import GaussianMixture\n",
        "\n",
        "\n",
        "# Fit models with 2 to 8 components\n",
        "models = []\n",
        "for n in range(2, 9):\n",
        "    model = GaussianMixture(n_components=n).fit(data)\n",
        "    models.append(model)\n",
        "\n",
        "# Plot the AIC, BIC, and ICL values\n",
        "import matplotlib.pyplot as plt\n",
        "plt.plot(range(2, 9), [m.aic(data) for m in models], label=\"AIC\")\n",
        "plt.plot(range(2, 9), [m.bic(data) for m in models], label=\"BIC\")\n",
        "plt.plot(range(2, 9), [m.lower_bound_ for m in models], label=\"ICL\")\n",
        "plt.xlabel(\"Number of components\")\n",
        "plt.ylabel(\"Value of information criteria\")\n",
        "plt.legend()\n",
        "plt.show()\n"
      ],
      "metadata": {
        "id": "_P3UFJH0e_I7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Fit the mixture model with 4 components\n",
        "model = GaussianMixture(n_components=4).fit(data)\n",
        "\n",
        "# Extract the cluster assignments\n",
        "clusters = model.predict(data)\n"
      ],
      "metadata": {
        "id": "ZQ4Fk-FBfgmL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.cluster import KMeans\n",
        "\n",
        "# Fit the k-means model with 4 clusters\n",
        "kmeans = KMeans(n_clusters=4).fit(data)\n",
        "\n",
        "# Compare the cluster assignments of the two models\n",
        "pd.crosstab(kmeans.labels_, clusters, rownames=[\"K-means\"], colnames=[\"Mixture\"])\n"
      ],
      "metadata": {
        "id": "RP_g7tb1fjA_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import statsmodels.api as sm\n",
        "\n",
        "# Assuming MD.reg2 is already defined and contains the logistic regression model\n",
        "\n",
        "# Refit the model\n",
        "MD_ref2 = sm.regression.linear_model.RegressionResults.fit(MD.reg2)\n",
        "\n",
        "# Print summary statistics\n",
        "print(MD_ref2.summary())\n"
      ],
      "metadata": {
        "id": "YcYtcJZjflbG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import rpy2.robjects as robjects\n",
        "from rpy2.robjects.packages import importr\n",
        "lattice = importr('lattice')\n",
        "\n",
        "# Convert MD.x to an R matrix\n",
        "MD_x = robjects.r['matrix'](robjects.FloatVector(MD.x), nrow=11, byrow=True)\n",
        "\n",
        "# Perform hierarchical clustering on the transpose of MD.x\n",
        "MD_vclust = robjects.r['hclust'](robjects.r['dist'](robjects.r['t'](MD_x)))\n",
        "\n",
        "# Create the segmented bar chart\n",
        "robjects.r['barchart'](MD_k4, shade=True, which=robjects.r['rev'](MD_vclust.rx('order')[0]))\n"
      ],
      "metadata": {
        "id": "8ZYa13_AggCy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "from scipy.spatial.distance import pdist, squareform\n",
        "from sklearn.cluster import KMeans\n",
        "from sklearn.decomposition import PCA\n",
        "from sklearn.manifold import MDS\n",
        "from sklearn.preprocessing import scale\n",
        "from scipy.cluster.hierarchy import dendrogram, linkage\n",
        "\n",
        "# Load data\n",
        "mcdonalds = pd.read_csv('mcdonalds.csv')\n",
        "\n",
        "# Subset data for clustering\n",
        "MD.x = mcdonalds.iloc[:, 2:13]\n",
        "\n",
        "# Perform hierarchical clustering\n",
        "MD.dist = pdist(MD.x.T, metric='euclidean')\n",
        "MD.hclust = linkage(MD.dist, method='ward')\n",
        "\n",
        "# Perform k-means clustering\n",
        "MD.k4 = KMeans(n_clusters=4, random_state=1).fit(MD.x)\n",
        "\n",
        "# Create mosaic plot of clustering results\n",
        "k4 = MD.k4.labels_\n",
        "table = pd.crosstab(k4, mcdonalds['Like'])\n",
        "table.plot(kind='bar', stacked=True, colormap='Pastel2')\n",
        "plt.title('Mosaic Plot of Clustering Results')\n",
        "plt.xlabel('Segment Number')\n",
        "plt.show()\n",
        "\n",
        "# Perform PCA\n",
        "MD.pca = PCA().fit(MD.x)\n",
        "MD.pca_scores = MD.pca.transform(MD.x)\n",
        "\n",
        "# Plot PCA scores\n",
        "plt.scatter(MD.pca_scores[:, 0], MD.pca_scores[:, 1], c=k4, cmap='Pastel2')\n",
        "plt.xlabel('Principal Component 1')\n",
        "plt.ylabel('Principal Component 2')\n",
        "plt.title('PCA Scores')\n",
        "plt.show()\n",
        "\n",
        "# Perform MDS\n",
        "MD.mds = MDS(n_components=2, dissimilarity='precomputed').fit_transform(squareform(MD.dist))\n",
        "\n",
        "# Plot MDS results\n",
        "plt.scatter(MD.mds[:, 0], MD.mds[:, 1], c=k4, cmap='Pastel2')\n",
        "plt.xlabel('MDS Dimension 1')\n",
        "plt.ylabel('MDS Dimension 2')\n",
        "plt.title('MDS Results')\n",
        "plt.show()\n",
        "\n",
        "# Plot dendrogram\n",
        "plt.figure(figsize=(10, 5))\n",
        "plt.title('Dendrogram')\n",
        "plt.xlabel('Segments')\n",
        "plt.ylabel('Distance')\n",
        "dendrogram(MD.hclust, leaf_rotation=90., leaf_font_size=8., labels=MD.x.columns.tolist())\n",
        "plt.show()\n"
      ],
      "metadata": {
        "id": "BLpt6SbAhBMA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "table = pd.crosstab(k4, mcdonalds['Gender'])\n",
        "\n",
        "# plot the mosaic plot\n",
        "plt.rcParams.update({'font.size': 12})\n",
        "plt.figure(figsize=(8, 6))\n",
        "plt.title('Segmentation by Gender')\n",
        "plt.mosaicplot(table, shade=True)\n",
        "plt.xlabel('Gender')\n",
        "plt.ylabel('Segment number')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "R_Lri8yQhmK4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from partykit import ctree, plot\n",
        "\n",
        "\n",
        "# Build the classification tree\n",
        "tree = ctree(\"(k4 == 3) ~ Like.n + Age + VisitFrequency + Gender\", data=mcdonalds)\n",
        "\n",
        "# Plot the tree\n",
        "plot(tree)\n",
        "\n",
        "# Compute mean values for each segment\n",
        "visit = mcdonalds.groupby(\"k4\")[\"VisitFrequency\"].mean()\n",
        "like = mcdonalds.groupby(\"k4\")[\"Like.n\"].mean()\n",
        "female = mcdonalds.groupby(\"k4\")[\"Gender\"].apply(lambda x: (x == \"Female\").mean())"
      ],
      "metadata": {
        "id": "pnM_tjRfhywh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "# Calculate mean visit frequency for each segment\n",
        "visit = mcdonalds.groupby('k4')['VisitFrequency'].mean()\n",
        "\n",
        "# Calculate mean like rating for each segment\n",
        "like = mcdonalds.groupby('k4')['Like.n'].mean()\n",
        "\n",
        "# Convert Gender to numeric and calculate mean for each segment\n",
        "female = mcdonalds.groupby('k4')['Gender'].apply(lambda x: (x == 'Female').mean())\n",
        "\n",
        "# Create scatter plot with bubble size based on female percentage\n",
        "plt.scatter(visit, like, s=female*100, alpha=0.5)\n",
        "\n",
        "# Add labels to each point\n",
        "for i in range(1, 5):\n",
        "    plt.text(visit[i], like[i], str(i))\n",
        "\n",
        "# Set x and y limits\n",
        "plt.xlim(2, 4.5)\n",
        "plt.ylim(-3, 3)\n",
        "\n",
        "# Add axis labels and title\n",
        "plt.xlabel('Visit Frequency')\n",
        "plt.ylabel('Like Rating')\n",
        "plt.title('Segment Evaluation Plot')\n",
        "\n",
        "# Show the plot\n",
        "plt.show()\n"
      ],
      "metadata": {
        "id": "FaeIo1oKiEtn"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
