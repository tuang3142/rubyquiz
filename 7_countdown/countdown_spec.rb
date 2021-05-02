require_relative "countdown"
require "rspec"

RSpec.describe Countdown do
  it "solves" do
    expect(Countdown.new.pop).to eq 1
  end

  it "solves" do
    expect(Countdown.new.pop).to eq 2
  end
end
