## ColorSyncLegacy

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ColorSyncLegacy.framework/Versions/A/ColorSyncLegacy`

```diff

-3777.0.0.0.0
-  __TEXT.__text: 0x738c
+3777.4.1.0.0
+  __TEXT.__text: 0x751c
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x9fb
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__unwind_info: 0x2c8
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0xca0
   __AUTH_CONST.__auth_got: 0x178

   - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 897165EF-990B-30AB-97B4-236EF55F1C09
-  Functions: 228
-  Symbols:   698
+  UUID: B36BAD3E-818F-3BB4-8100-D8B8AD04ED5A
+  Functions: 329
+  Symbols:   799
   CStrings:  117
 
Symbols:
+ CMCloneProfileRef.cold.1
+ CMCloseProfile.cold.1
+ CMConvertDoubleXYZToD50.cold.1
+ CMConvertRGBFloatBitmap.cold.1
+ CMConvertXYZFloatBitmap.cold.1
+ CMCopyProfile.cold.1
+ CMCopyProfileDescriptionString.cold.1
+ CMCopyProfileLocalizedString.cold.1
+ CMCopyProfileLocalizedStringDictionary.cold.1
+ CMCountProfileElements.cold.1
+ CMFloatBitmapMakeChunky.cold.1
+ CMGetColorSyncVersion.cold.1
+ CMGetDefaultDevice.cold.1
+ CMGetDefaultProfileBySpace.cold.1
+ CMGetDefaultProfileByUse.cold.1
+ CMGetDeviceDefaultProfileID.cold.1
+ CMGetDeviceFactoryProfiles.cold.1
+ CMGetDeviceInfo.cold.1
+ CMGetDeviceProfile.cold.1
+ CMGetDeviceState.cold.1
+ CMGetDeviceTrackingByUse.cold.1
+ CMGetGammaByAVID.cold.1
+ CMGetIndNamedColorValue.cold.1
+ CMGetIndProfileElement.cold.1
+ CMGetIndProfileElementInfo.cold.1
+ CMGetNamedColorIndex.cold.1
+ CMGetNamedColorInfo.cold.1
+ CMGetNamedColorName.cold.1
+ CMGetNamedColorValue.cold.1
+ CMGetPS2ColorRendering.cold.1
+ CMGetPS2ColorRenderingIntent.cold.1
+ CMGetPS2ColorRenderingVMSize.cold.1
+ CMGetPS2ColorSpace.cold.1
+ CMGetPartialProfileElement.cold.1
+ CMGetProfileByAVID.cold.1
+ CMGetProfileDescriptions.cold.1
+ CMGetProfileElement.cold.1
+ CMGetProfileGamma.cold.1
+ CMGetProfileHeader.cold.1
+ CMGetProfileLocation.cold.1
+ CMGetProfileMD5.cold.1
+ CMGetProfileRefCount.cold.1
+ CMGetProfileTransformInfo.cold.1
+ CMGetSystemProfile.cold.1
+ CMGetSystemProfileAVID.cold.1
+ CMGetSystemProfilePriv.cold.1
+ CMIterateCMMInfo.cold.1
+ CMIterateColorDevices.cold.1
+ CMIterateColorSyncFolder.cold.1
+ CMIterateDeviceProfiles.cold.1
+ CMMakeProfile.cold.1
+ CMMatchFloatBitmap.cold.1
+ CMNewProfile.cold.1
+ CMOpenProfile.cold.1
+ CMProfileCopyICCData.cold.1
+ CMProfileElementExists.cold.1
+ CMProfileModified.cold.1
+ CMRegisterColorDevice.cold.1
+ CMRemoveProfileElement.cold.1
+ CMSetDefaultDevice.cold.1
+ CMSetDeviceDefaultProfileID.cold.1
+ CMSetDeviceFactoryProfiles.cold.1
+ CMSetDeviceProfile.cold.1
+ CMSetDeviceState.cold.1
+ CMSetDeviceTrackingByUse.cold.1
+ CMSetGammaByAVID.cold.1
+ CMSetPartialProfileElement.cold.1
+ CMSetProfileByAVID.cold.1
+ CMSetProfileDescriptions.cold.1
+ CMSetProfileElement.cold.1
+ CMSetProfileElementReference.cold.1
+ CMSetProfileElementSize.cold.1
+ CMSetProfileHeader.cold.1
+ CMSetProfileLocalizedStringDictionary.cold.1
+ CMSetSystemProfile.cold.1
+ CMSetSystemProfileAVID.cold.1
+ CMUnregisterColorDevice.cold.1
+ CMUpdateProfile.cold.1
+ CMValidateProfile.cold.1
+ CWCheckBitmap.cold.1
+ CWCheckColors.cold.1
+ CWColorWorldGetProperty.cold.1
+ CWColorWorldSetProperty.cold.1
+ CWConcatColorWorld.cold.1
+ CWDisposeColorWorld.cold.1
+ CWFillLookupTexture.cold.1
+ CWGetCMMSignature.cold.1
+ CWMatchBitmap.cold.1
+ CWMatchColors.cold.1
+ CWNewLinkProfile.cold.1
+ ColorSyncLog.cold.2
+ NCMGetProfileLocation.cold.1
+ NCWConcatColorWorld.cold.1
+ NCWNewColorWorld.cold.1
+ NCWNewLinkProfile.cold.1
+ _CMGetProfileOfSuite.cold.1
+ _CMLoadProfileLutsByAVID.cold.1
+ _CMProfileGetProperty.cold.1
+ _CMProfileSetProperty.cold.1
+ _CWColorWorldGetProperty.cold.1
+ _CWColorWorldSetProperty.cold.1

```
