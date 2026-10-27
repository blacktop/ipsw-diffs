## com.apple.AppleSunriseBluetooth

> `/System/Library/DriverExtensions/com.apple.AppleSunriseBluetooth.dext/com.apple.AppleSunriseBluetooth`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-112.0.0.0.0
-  __TEXT.__text: 0x2e9e8
+113.0.0.0.0
+  __TEXT.__text: 0x2eb58
   __TEXT.__auth_stubs: 0x930
   __TEXT.__cstring: 0xb3e9
   __TEXT.__const: 0x15b0
-  __TEXT.__unwind_info: 0xd68
+  __TEXT.__unwind_info: 0xd60
   __TEXT.__oslogstring: 0x251d
   __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__osclassinfo: 0x60
Functions:
~ __ZN21AppleSunriseHALClient32InvokeHALEventHandlerType_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSAction24AppleSunriseHALEventTypeP6OSDataEPK11OSMetaClass : 268 -> 292
~ __ZN21AppleSunriseHALClient37InvokeTimeSyncGPIOEventHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSActionhyEPK11OSMetaClass : 236 -> 264
~ __ZN21AppleSunriseHALClient30RegisterHALEventHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSActionE : 220 -> 244
~ __ZN21AppleSunriseHALClient26AppleSunrisePCIeFLR_InvokeE5IORPCP15OSMetaClassBasePFiS2_E : 148 -> 200
~ __ZN21AppleSunriseHALClient27AppleSunriseSoCReset_InvokeE5IORPCP15OSMetaClassBasePFiS2_E : 148 -> 200
~ __ZN21AppleSunriseHALClient39RegisterTimeSyncGPIOEventHandler_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSActionP8OSStringE : 252 -> 276
~ __ZN21AppleSunriseHALClient41AppleSunriseSetFunctionCrashAction_InvokeE5IORPCP15OSMetaClassBasePFvS2_34AppleSunriseHALFunctionCrashActionE : 124 -> 168
~ __ZN21AppleSunriseHALClient18getLPMState_InvokeE5IORPCP15OSMetaClassBasePFiS2_E : 148 -> 200
~ __ZN21AppleSunriseHALClient23halGetDTProperty_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSStringS4_PP6OSDataE : 280 -> 304
~ __ZN21AppleSunriseHALClient29reportCurrentDextStage_InvokeE5IORPCP15OSMetaClassBasePFvS2_24AppleSunriseHALDextStageE : 124 -> 168
```
