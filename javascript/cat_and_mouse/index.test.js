// catAndMouse.test.js
const catAndMouse = require('./index');

// Test case 1: Cats are equidistant from the mouse
test('Cats are equidistant from the mouse', () => {
  expect(catAndMouse(2, 2, 3)).toBe('Mouse C');
});

// Test case 2: Cat A catches the mouse first
test('Cat A catches the mouse first', () => {
  expect(catAndMouse(1, 4, 2)).toBe('Cat A');
});

// Test case 3: Cat B catches the mouse first
test('Cat B catches the mouse first', () => {
  expect(catAndMouse(5, 2, 0)).toBe('Cat B');
});
