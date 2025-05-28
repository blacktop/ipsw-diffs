## RespiratoryHealth

> `/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x644c
-  __TEXT.__auth_stubs: 0x3d0
+4146.4.18.0.0
+  __TEXT.__text: 0x60f0
+  __TEXT.__auth_stubs: 0x3b0
   __TEXT.__objc_methlist: 0x7a0
   __TEXT.__const: 0x50
-  __TEXT.__oslogstring: 0xa41
-  __TEXT.__cstring: 0x757
+  __TEXT.__oslogstring: 0x9f4
+  __TEXT.__cstring: 0x735
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x268
-  __TEXT.__objc_classname: 0x321
-  __TEXT.__objc_methname: 0x1e75
+  __TEXT.__unwind_info: 0x26c
+  __TEXT.__objc_classname: 0x34e
+  __TEXT.__objc_methname: 0x1e01
   __TEXT.__objc_methtype: 0x55a
-  __TEXT.__objc_stubs: 0x1380
+  __TEXT.__objc_stubs: 0x12c0
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x60
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1680
-  __DATA_CONST.__objc_selrefs: 0x6d8
-  __AUTH_CONST.__objc_const: 0x4b8
-  __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__objc_const: 0x1670
+  __DATA_CONST.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_arraydata: 0x28
+  __AUTH_CONST.__objc_const: 0x4f8
+  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x1e8
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x130
-  __DATA.__objc_superrefs: 0x60
   __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x360
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 194
-  Symbols:   851
-  CStrings:  483
+  Functions: 193
+  Symbols:   845
+  CStrings:  476
 
Symbols:
+ +[HKCountrySet(HKFeatureIdentifierOxygenSaturationRecording) localAvailabilityForHKFeatureIdentifierOxygenSaturationRecording]
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ __OBJC_$_CATEGORY_HKCountrySet_$_HKFeatureIdentifierOxygenSaturationRecording
+ __OBJC_$_CLASS_METHODS_HKCountrySet(HKFeatureIdentifierOxygenSaturationRecording)
+ ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.243
+ ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.249
+ ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.260
+ __unnamed_array_storage.252
+ _objc_msgSend$initWithCountryBitmasks:compatibilityVersion:contentVersion:provenance:
+ _objc_msgSend$localAvailabilityForHKFeatureIdentifierOxygenSaturationRecording
- +[HKRPOxygenSaturationAvailability _availabilityPlistURL]
- +[HKRPOxygenSaturationAvailability allowedCountryCodesByVersion]
- _GSSystemRootDirectory
- _OBJC_CLASS_$_NSURL
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.219
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.225
- ___63-[HKRPOxygenSaturationOnboardingManager onboardWithCompletion:]_block_invoke.236
- __os_log_fault_impl
- _objc_msgSend$URLByAppendingPathComponent:
- _objc_msgSend$URLByAppendingPathExtension:
- _objc_msgSend$_availabilityPlistURL
- _objc_msgSend$countrySetWithPlistURL:error:
- _objc_msgSend$fileURLWithPath:isDirectory:
- _objc_msgSend$isAppleInternalInstall
- _objc_msgSend$regionsWithPlistAtURL:error:
- _objc_msgSend$stringByAppendingString:
CStrings:
+ "HKCountrySet+HKFeatureIdentifierOxygenSaturationRecording.m"
+ "HKFeatureIdentifierOxygenSaturationRecording"
+ "Local generated country set should never be nil"
+ "Q"
+ "T@\"NSString\",?,R,C"
+ "i"
+ "initWithCountryBitmasks:compatibilityVersion:contentVersion:provenance:"
+ "localAvailabilityForHKFeatureIdentifierOxygenSaturationRecording"
- "/System/Library/Health/AvailableRegions"
- "Availability plist is a static file that should exist. Error: %@"
- "HKRPOxygenSaturationAvailability.m"
- "T@\"NSDictionary\",R,N"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathExtension:"
- "[%{public}@] %{public}@ Could not read availability plist. Error: %{public}@"
- "_availabilityPlistURL"
- "allowedCountryCodesByVersion"
- "countrySetWithPlistURL:error:"
- "fileURLWithPath:isDirectory:"
- "isAppleInternalInstall"
- "plist"
- "regionsWithPlistAtURL:error:"
- "stringByAppendingString:"

```
