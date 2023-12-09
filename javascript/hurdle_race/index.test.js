const hurdleRace = require('./index');

describe('hurdleRace', () => {
  it('should return the minimum doses of magic potion needed to clear the hurdles', () => {
    // Test case 1
    const result1 = hurdleRace(4, [1, 6, 3, 5, 2]);
    expect(result1).toBe(2);

    // Test case 2
    const result2 = hurdleRace(7, [2, 5, 4, 8, 9]);
    expect(result2).toBe(2);
  });
});
