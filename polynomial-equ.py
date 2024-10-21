{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOv6S4rV3dIhoopywmbaUJM",
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
        "<a href=\"https://colab.research.google.com/github/Sumaira-Ashraf/quadartic-eq/blob/main/polynomial-equ.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import sympy as sp\n",
        "\n",
        "# Function to solve linear equations\n",
        "def solve_linear(a, b):\n",
        "    if a == 0:\n",
        "        return \"No solution (a cannot be 0 for a linear equation)\"\n",
        "    return -b / a\n",
        "\n",
        "# Function to solve polynomial equations\n",
        "def solve_polynomial(coefficients):\n",
        "    x = sp.symbols('x')\n",
        "    polynomial = sum([coeff * x**i for i, coeff in enumerate(coefficients)])\n",
        "    solutions = sp.solve(polynomial, x)\n",
        "    return polynomial, solutions\n",
        "\n",
        "# Function to plot the equation (linear or polynomial)\n",
        "def plot_equation(coefficients, solutions, title):\n",
        "    x_vals = np.linspace(-10, 10, 400)\n",
        "    y_vals = sum([coeff * x_vals**i for i, coeff in enumerate(coefficients)])\n",
        "\n",
        "    plt.figure(figsize=(6, 4))\n",
        "    plt.plot(x_vals, y_vals, label=f'{title}')\n",
        "    plt.axhline(0, color='black', linewidth=0.5)\n",
        "    plt.axvline(0, color='black', linewidth=0.5)\n",
        "    plt.grid(True)\n",
        "\n",
        "    # Highlight the roots if they exist\n",
        "    if solutions:\n",
        "        for root in solutions:\n",
        "            if sp.im(root) == 0:  # Plot only real solutions\n",
        "                plt.scatter(float(root), 0, color='red')\n",
        "                plt.text(float(root), 0, f'Root: {float(root):.2f}', color='red', fontsize=10)\n",
        "\n",
        "    plt.title(f'Graph of {title}')\n",
        "    plt.xlabel('x')\n",
        "    plt.ylabel('f(x)')\n",
        "    plt.legend()\n",
        "    st.pyplot(plt)\n",
        "\n",
        "# Streamlit app\n",
        "st.title(\"Equation Solver and Visualizer\")\n",
        "\n",
        "# Choose the type of equation\n",
        "equation_type = st.selectbox(\"Choose the type of equation\", [\"Linear\", \"Polynomial\"])\n",
        "\n",
        "if equation_type == \"Linear\":\n",
        "    st.subheader(\"Solve a Linear Equation (ax + b = 0)\")\n",
        "\n",
        "    # Input for linear equation coefficients\n",
        "    a = st.number_input(\"Enter the coefficient a (for x):\", value=1.0)\n",
        "    b = st.number_input(\"Enter the constant b:\", value=0.0)\n",
        "\n",
        "    # Solve the linear equation\n",
        "    if a != 0:\n",
        "        solution = solve_linear(a, b)\n",
        "        st.write(f\"The solution is: x = {solution}\")\n",
        "\n",
        "        # Plot the linear equation\n",
        "        plot_equation([b, a], [solution], f'{a}x + {b} = 0')\n",
        "    else:\n",
        "        st.write(\"Coefficient 'a' cannot be 0 for a linear equation.\")\n",
        "\n",
        "elif equation_type == \"Polynomial\":\n",
        "    st.subheader(\"Solve a Polynomial Equation\")\n",
        "\n",
        "    # Input for the degree of the polynomial\n",
        "    degree = st.number_input(\"Enter the degree of the polynomial:\", min_value=1, value=2, step=1)\n",
        "\n",
        "    # Input for polynomial coefficients\n",
        "    coefficients = []\n",
        "    for i in range(degree, -1, -1):\n",
        "        coeff = st.number_input(f\"Enter the coefficient for x^{i}:\", value=0.0)\n",
        "        coefficients.append(coeff)\n",
        "\n",
        "    coefficients.reverse()  # Reverse to match the correct power order\n",
        "\n",
        "    # Solve the polynomial equation\n",
        "    polynomial, solutions = solve_polynomial(coefficients)\n",
        "\n",
        "    st.write(f\"The polynomial is: {polynomial} = 0\")\n",
        "    st.write(f\"The solutions are: {solutions}\")\n",
        "\n",
        "    # Plot the polynomial equation\n",
        "    plot_equation(coefficients, solutions, f'{polynomial} = 0')\n"
      ],
      "metadata": {
        "id": "NS_8OXhhKJ39"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}