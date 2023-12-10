const getMoneySpent = require('./index');

test('getMoneySpent', () => {
    expect(getMoneySpent([40,50,60], [5,8,12], 60)).toBe(58);
});


test('getMoneySpent b', () => {
    expect(getMoneySpent([4], [5], 5)).toBe(-1);
});
