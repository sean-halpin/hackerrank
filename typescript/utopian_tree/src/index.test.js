"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const index_1 = require("./index");
describe('utopianTree', () => {
    // Test case 1: When n is 0
    it('should return 1 when n is 0', () => {
        expect((0, index_1.utopianTree)(0)).toBe(1);
    });
    it('should return 7 when n is 4', () => {
        expect((0, index_1.utopianTree)(4)).toBe(7);
    });
    it('should return 6 when n is 3', () => {
        expect((0, index_1.utopianTree)(3)).toBe(6);
    });
});
