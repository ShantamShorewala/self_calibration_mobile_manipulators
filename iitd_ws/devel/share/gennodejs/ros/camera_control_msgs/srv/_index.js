
"use strict";

let SetGamma = require('./SetGamma.js')
let SetBrightness = require('./SetBrightness.js')
let SetBinning = require('./SetBinning.js')
let SetGain = require('./SetGain.js')
let SetExposure = require('./SetExposure.js')
let SetBool = require('./SetBool.js')
let SetROI = require('./SetROI.js')
let SetSleeping = require('./SetSleeping.js')
let GetCamProperties = require('./GetCamProperties.js')

module.exports = {
  SetGamma: SetGamma,
  SetBrightness: SetBrightness,
  SetBinning: SetBinning,
  SetGain: SetGain,
  SetExposure: SetExposure,
  SetBool: SetBool,
  SetROI: SetROI,
  SetSleeping: SetSleeping,
  GetCamProperties: GetCamProperties,
};
