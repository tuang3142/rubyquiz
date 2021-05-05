require_relative "solution"
require "rspec"

RSpec.describe Solution do
  context "basic case" do
    it "solves" do
      grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
      ]

      result = Solution.new(grid).solve
      expect(result).to eq 3
    end
  end

  context "edge case" do
    it "solves" do
      grid = [["0"]]

      result = Solution.new(grid).solve
      expect(result).to eq 0
    end
  end
end
