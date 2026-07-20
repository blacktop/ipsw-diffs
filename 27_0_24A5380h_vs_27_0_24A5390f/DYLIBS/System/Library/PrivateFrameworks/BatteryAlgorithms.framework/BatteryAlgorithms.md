## BatteryAlgorithms

> `/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-142.0.0.0.0
-  __TEXT.__text: 0x800b8
+146.0.0.0.0
+  __TEXT.__text: 0x80550
   __TEXT.__objc_methlist: 0xb04
-  __TEXT.__const: 0xa9e0
-  __TEXT.__cstring: 0x3ecb
-  __TEXT.__gcc_except_tab: 0x8734
+  __TEXT.__const: 0xa9d0
+  __TEXT.__cstring: 0x3ef2
+  __TEXT.__gcc_except_tab: 0x8770
   __TEXT.__oslogstring: 0xc5
   __TEXT.__unwind_info: 0x2920
   __TEXT.__objc_stubs: 0x0

   __AUTH_CONST.__auth_got: 0x428
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x13c
-  __DATA.__data: 0x74dfe0
+  __DATA.__data: 0x7ba230
   __DATA.__common: 0xe
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2104
-  Symbols:   4181
-  CStrings:  620
+  Symbols:   4219
+  CStrings:  621
 
Symbols:
+ _gACAMAgingModelParameterV159ATL
+ _gACAMAgingModelParameterV159LGC
+ _gACAMAgingTableV159ATL
+ _gACAMAgingTableV159LGC
+ _gACAMAgingUpdatorParameterV159ATL
+ _gACAMAgingUpdatorParameterV159LGC
+ _gACAMCommonParameterV159ATL
+ _gACAMCommonParameterV159LGC
+ _gACAMConfigurationV159ATL
+ _gACAMConfigurationV159LGC
+ _gCRateChgGridRawDataV159ATL
+ _gCRateChgGridRawDataV159LGC
+ _gCRateDcgGridRawDataV159ATL
+ _gCRateDcgGridRawDataV159LGC
+ _gCRateDcgRawDataV159ATL
+ _gCRateDcgRawDataV159LGC
+ _gOcpNegRawDataV159ATL
+ _gOcpNegRawDataV159LGC
+ _gOcpPosRawDataV159ATL
+ _gOcpPosRawDataV159LGC
+ _gResistanceNegChgRawDataV159ATL
+ _gResistanceNegChgRawDataV159LGC
+ _gResistanceNegDcgRawDataV159ATL
+ _gResistanceNegDcgRawDataV159LGC
+ _gResistancePosChgRawDataV159ATL
+ _gResistancePosChgRawDataV159LGC
+ _gResistancePosDcgRawDataV159ATL
+ _gResistancePosDcgRawDataV159LGC
+ _gSocGridRawDataV159ATL
+ _gSocGridRawDataV159LGC
+ _gTempGridRawDataV159ATL
+ _gTempGridRawDataV159LGC
+ _gWRaFreshRawDataV159ATL
+ _gWRaFreshRawDataV159LGC
+ _gWRcFreshRawDataV159ATL
+ _gWRcFreshRawDataV159LGC
+ _gYShrinkV159ATL
+ _gYShrinkV159LGC
Functions:
~ __ZN11ACAMUtility17ACAMParameterPackC2ENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 13088 -> 13856
~ -[CafeLVR init:] : 2172 -> 2192
~ -[CafeLVR getCafeLVRConfig] : 1416 -> 1428
~ -[CafeLVR snapshot] : 80 -> 76
~ -[CafeLVR .cxx_construct] : 24 -> 28
~ __ZN19LowVoltageResidency15PersistentState19getTypeErasedConfigEv : 4568 -> 4720
~ __ZN19LowVoltageResidency6EngineC2Ev : 3488 -> 3656
~ __ZN19LowVoltageResidency6Engine10runOneStepExxb : 364 -> 372
~ __ZN19LowVoltageResidency6Engine21exportPersistentStateEv : 128 -> 152
~ __ZN19LowVoltageResidency6Engine21importPersistentStateERNS_15PersistentStateE : 108 -> 124
~ __ZNK14ACAMAgingModel18calculateAgingRateERK16ACAMBatteryStateRK18ACAMElectrodeStateRK14ACAMAgingStateR14ACAMDerivative : 868 -> 876
CStrings:
+ "\n{\n  \"Lifetime\": {\n    \"controller\": {\n      \"Ki\": 8e-10,\n      \"Kp\": 0.0005,\n      \"u_max\": 1,\n      \"u_min\": 0\n    },\n    \"settings\": {\n      \"shape\": {\n        \"a\": 0,\n        \"b\": 5.7519e-05,\n        \"c\": 2.9304e+03\n      }\n    },\n    \"enable\": 1,\n    \"interval\": 86400\n  },\n  \"ProjectedLifetime\": {\n    \"controller\": {\n      \"Ki\": 0,\n      \"Kp\": 2.00e-03,\n      \"u_max\": 1,\n      \"u_min\": 0\n    },\n    \"settings\": {\n      \"epsilon\": 0.000694444,\n      \"lambda\": 0.85\n    },\n    \"enable\": 0,\n    \"interval\": 86400\n  },\n  \"SafeHarbor\": {\n    \"aged_target\": {\n      \"debounce_time\": 8,\n      \"socv\": 3.2\n    },\n    \"swell_target\": {\n      \"debounce_time\": 8,\n      \"socv\": 3.2\n    }\n  },\n  \"Weekly\": {\n    \"controller\": {\n      \"Ki\": 0,\n      \"Kp\": 3.33e-02,\n      \"u_max\": 1,\n      \"u_min\": 0\n    },\n    \"settings\": {\n      \"shape\": {\n        \"a\": 0,\n        \"b\": 0,\n        \"c\": 46.15384615\n      }\n    },\n    \"enable\": 0,\n    \"interval\": 604800\n  },\n  \"control_effort_table\": {\n    \"control_effort\": [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],\n    \"debounce_time\": [8,8,8,8,8,8,8,8,8,8,8],\n    \"socv\": [3,3.1,3.12,3.13,3.14,3.15,3.16,3.17,3.18,3.19,3.2]\n  },\n  \"final_budget_target\": 12000,\n  \"final_time\": 157680000,\n  \"max_interval\": 1209600,\n  \"grace_period\": 1209600,\n  \"grace_period_budget_target\": 3000,\n  \"control_effort_slew_rate_up\": 0.02,\n  \"control_effort_slew_rate_down\": 0.1,\n  \"weights\": [[[0,1,1],[0,1,1],[0,1,1]],[[0,1,1],[0,1,1],[0,1,1]],[[0,0,0],[0,0,0],[0,0,0]]],\n  \"config_version\": 1,\n}\n"
+ "config_version"
- "\n{\n  \"Lifetime\": {\n    \"controller\": {\n      \"Ki\": 8e-10,\n      \"Kp\": 0.0005,\n      \"u_max\": 1,\n      \"u_min\": 0\n    },\n    \"settings\": {\n      \"shape\": {\n        \"a\": 0,\n        \"b\": 5.7519e-05,\n        \"c\": 2.9304e+03\n      }\n    },\n    \"enable\": 1,\n    \"interval\": 86400\n  },\n  \"ProjectedLifetime\": {\n    \"controller\": {\n      \"Ki\": 0,\n      \"Kp\": 2.00e-03,\n      \"u_max\": 1,\n      \"u_min\": 0\n    },\n    \"settings\": {\n      \"epsilon\": 0.000694444,\n      \"lambda\": 0.85\n    },\n    \"enable\": 0,\n    \"interval\": 86400\n  },\n  \"SafeHarbor\": {\n    \"aged_target\": {\n      \"debounce_time\": 8,\n      \"socv\": 3.2\n    },\n    \"swell_target\": {\n      \"debounce_time\": 8,\n      \"socv\": 3.2\n    }\n  },\n  \"Weekly\": {\n    \"controller\": {\n      \"Ki\": 0,\n      \"Kp\": 3.33e-02,\n      \"u_max\": 1,\n      \"u_min\": 0\n    },\n    \"settings\": {\n      \"shape\": {\n        \"a\": 0,\n        \"b\": 0,\n        \"c\": 46.15384615\n      }\n    },\n    \"enable\": 0,\n    \"interval\": 604800\n  },\n  \"control_effort_table\": {\n    \"control_effort\": [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],\n    \"debounce_time\": [8,8,8,8,8,8,8,8,8,8,8],\n    \"socv\": [3,3.1,3.12,3.13,3.14,3.15,3.16,3.17,3.18,3.19,3.2]\n  },\n  \"final_budget_target\": 12000,\n  \"final_time\": 157680000,\n  \"max_interval\": 1209600,\n  \"grace_period\": 1209600,\n  \"grace_period_budget_target\": 3000,\n  \"control_effort_slew_rate_up\": 0.02,\n  \"control_effort_slew_rate_down\": 0.1,\n  \"weights\": [[[1,1,1],[1,1,1],[1,1,1]],[[1,1,1],[1,1,1],[1,1,1]],[[0,0,0],[0,0,0],[0,0,0]]]\n}\n"
```
