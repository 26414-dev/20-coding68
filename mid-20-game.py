{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP39RXQtr6UryHhGrCLLdHC",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/26414-dev/20-coding68/blob/main/mid-20-game.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "19/12/68"
      ],
      "metadata": {
        "id": "jxcb3QtUrIiD"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 46,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5ghJWCXZps1N",
        "outputId": "f15a94a8-2337-49e4-a298-293451307af4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "รับข้อมูลราคาสินค้า100\n",
            "มีค่าส่ง\n"
          ]
        }
      ],
      "source": [
        "price = int(input(\"รับข้อมูลราคาสินค้า\"))\n",
        "\n",
        "VAT = 0.7\n",
        "total = (price * VAT)\n",
        "\n",
        "if total > 1000:\n",
        "  __builtins__.print(\"ฟรีค่าส่ง\")\n",
        "\n",
        "else:\n",
        "  __builtins__.print(\"มีค่าส่ง\")"
      ]
    }
  ]
}