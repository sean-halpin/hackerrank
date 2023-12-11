# Typescript Hackerranks Solutions

Initialize a new Proj 

```
mkdir proj_name
cd proj_name
npm init -y
npm install --save-dev typescript
npx tsc --init
npm i --save-dev @types/node
npm install --save-dev jest ts-jest @types/jest
```

# package.json
```
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "test": "tsc && npx jest --detectOpenHandles"
  },
  "jest": {
    "transform": {
      "^.+\\.tsx?$": "ts-jest"
    }
  },
```

# Run Tests

```
npm test
```