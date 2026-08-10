## nfcd

> `/usr/libexec/nfcd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-370.40.2.0.0
-  __TEXT.__text: 0x1e71b0
-  __TEXT.__auth_stubs: 0x1860
+370.42.1.0.0
+  __TEXT.__text: 0x1e854c
+  __TEXT.__auth_stubs: 0x1880
   __TEXT.__delay_stubs: 0x540
   __TEXT.__delay_helper: 0x172c
-  __TEXT.__objc_stubs: 0xdf40
-  __TEXT.__objc_methlist: 0x9d9c
-  __TEXT.__const: 0x144c
-  __TEXT.__cstring: 0x22880
-  __TEXT.__oslogstring: 0x205b3
+  __TEXT.__objc_stubs: 0xe060
+  __TEXT.__objc_methlist: 0x9de4
+  __TEXT.__const: 0x145c
+  __TEXT.__cstring: 0x22a48
+  __TEXT.__oslogstring: 0x20776
   __TEXT.__objc_classname: 0x1d44
-  __TEXT.__objc_methname: 0x158cd
+  __TEXT.__objc_methname: 0x15a48
   __TEXT.__objc_methtype: 0x4e1f
-  __TEXT.__unwind_info: 0x2c48
+  __TEXT.__unwind_info: 0x2c58
   __DATA_CONST.__const: 0x9a50
-  __DATA_CONST.__cfstring: 0x11320
+  __DATA_CONST.__cfstring: 0x113a0
   __DATA_CONST.__objc_classlist: 0x650
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x388
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x480
-  __DATA_CONST.__objc_intobj: 0x7bf0
-  __DATA_CONST.__objc_arraydata: 0x1e58
+  __DATA_CONST.__objc_intobj: 0x7c20
+  __DATA_CONST.__objc_arraydata: 0x1e70
   __DATA_CONST.__objc_dictobj: 0x1040
-  __DATA_CONST.__objc_arrayobj: 0x318
-  __DATA_CONST.__auth_got: 0xce0
-  __DATA_CONST.__got: 0xa00
+  __DATA_CONST.__objc_arrayobj: 0x360
+  __DATA_CONST.__auth_got: 0xcf0
+  __DATA_CONST.__got: 0xa08
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x14ea8
-  __DATA.__objc_selrefs: 0x4b78
-  __DATA.__objc_ivar: 0x1134
+  __DATA.__objc_const: 0x14ec8
+  __DATA.__objc_selrefs: 0x4bc8
+  __DATA.__objc_ivar: 0x1138
   __DATA.__objc_data: 0x3f20
-  __DATA.__data: 0x2b34
+  __DATA.__data: 0x2b3c
   __DATA.__bss: 0x2c0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4274
-  Symbols:   671
-  CStrings:  11389
+  Functions: 4281
+  Symbols:   673
+  CStrings:  11419
 
Symbols:
+ _NFDriverSetReaderModeDynamicBBA
+ _NFPlatformHasAlternateRFSettingsForPACE
CStrings:
+ "%{public}s:%i Applying specialized PACE reader RF tuning"
+ "%{public}s:%i Default forcePaceRFSettings override"
+ "%{public}s:%i Failed to disable dynamic BBA: %{public}@"
+ "%{public}s:%i Failed to re-enable dynamic BBA: %{public}@"
+ "%{public}s:%i Mobile Asset specialized PACE global override"
+ "%{public}s:%i Overriding known bad wireless ECP frame to terminal type other"
+ "%{public}s:%i PACE config enabled"
+ "%{public}s:%i Reverting specialized PACE reader RF tuning"
+ "+[NFATLMobileSettings paceStaticRFAlwaysOn]"
+ "+[NFATLMobileSettings paceStaticRFBundleIds]"
+ "-[NFFieldNotificationECP1_0 initWithDictionary:]"
+ "-[_NFReaderSession _isSpecializedPACEReadingCoreNfcConfig:]"
+ "-[_NFReaderSession _isSpecializedPACEReadingInternalConfig:]"
+ "-[_NFReaderSession prepareForSpecializedPACEReading]"
+ "-[_NFReaderSession revertSpecializedPACEReading]"
+ "NFCD built from (B&I) Stockholm_Base-370.42.1"
+ "PACE_STATIC_RF_ALWAYS_ON"
+ "PACE_STATIC_RF_BUNDLE_IDS"
+ "_didApplySpecializedPACEReading"
+ "_isSpecializedPACEReadingCoreNfcConfig:"
+ "_isSpecializedPACEReadingInternalConfig:"
+ "forcePaceRFSettings"
+ "fr.gouv.france-identite"
+ "pace"
+ "paceStaticRFAlwaysOn"
+ "paceStaticRFBundleIds"
+ "prepareForSpecializedPACEReading"
+ "rangeOfString:options:"
+ "revertSpecializedPACEReading"
+ "setReaderModeDynamicBBA:staticBBA:"
+ "startISO18013WithConnectionHandoverConfiguration:type:credentialType:deviceCAParameters:delegate:"
- "NFCD built from (B&I) Stockholm_Base-370.40.2"
```
