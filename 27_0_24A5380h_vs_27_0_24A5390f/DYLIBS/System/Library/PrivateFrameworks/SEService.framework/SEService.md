## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/SEService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-70.35.1.0.0
-  __TEXT.__text: 0x113e68
-  __TEXT.__objc_methlist: 0x3c8c
+70.37.0.0.0
+  __TEXT.__text: 0x11433c
+  __TEXT.__objc_methlist: 0x3cb4
   __TEXT.__const: 0x18930
   __TEXT.__gcc_except_tab: 0x1ac8
-  __TEXT.__cstring: 0x8d65
-  __TEXT.__oslogstring: 0x2db7
+  __TEXT.__cstring: 0x8e75
+  __TEXT.__oslogstring: 0x2e57
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__swift5_typeref: 0x4430
   __TEXT.__constg_swiftt: 0x3a0c

   __TEXT.__swift_as_cont: 0x374
   __TEXT.__swift5_capture: 0x1e4
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x5360
+  __TEXT.__unwind_info: 0x5388
   __TEXT.__eh_frame: 0x6700
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b18
+  __DATA_CONST.__objc_selrefs: 0x1b68
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__got: 0x740
   __AUTH_CONST.__const: 0xa9f0
-  __AUTH_CONST.__cfstring: 0x4560
-  __AUTH_CONST.__objc_const: 0x83d0
+  __AUTH_CONST.__cfstring: 0x46a0
+  __AUTH_CONST.__objc_const: 0x83f8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x1040
   __AUTH.__objc_data: 0x7c0
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x38c
+  __DATA.__objc_ivar: 0x390
   __DATA.__data: 0x3750
   __DATA.__bss: 0x1c790
   __DATA.__common: 0x40

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7225
-  Symbols:   5301
-  CStrings:  1340
+  Functions: 7228
+  Symbols:   5316
+  CStrings:  1353
 
Symbols:
+ -[SEProxyWithManagerSession _checkPairing:]
+ -[SEProxyWithManagerSession validatePairing:callback:]
+ -[SEProxyWithRemoteTransceiver validatePairing:callback:]
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_IVAR_$_SESTapToRadar._pendingRequestTimestamp
+ _objc_msgSend$_checkPairing:
+ _objc_msgSend$deleteAllApplets:error:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$validateSEPairings:
CStrings:
+ "%@\n\n"
+ "EEE MMM d HH:mm:ss yyyy"
+ "Failed pairing check 1"
+ "Failed to deleteAllApplets"
+ "Failed to recheck after deleteAll %d %@"
+ "Got ambiguous pairing result %d"
+ "Issue Time: %@\n\n"
+ "Missing key and/or applet identifier"
+ "Missing key identifier"
+ "Pairing state (after) %{public}x / %{public}@"
+ "Pairing state (before) %{public}x / %{public}@"
+ "Please fill out the following information to assist with triage:\n\nVehicle Make:\nVehicle Model:\nAdditional Context:"
+ "STSRemoteTransceiver doesn't support validatePairing"
+ "Validate pairing re-paired with result %{public}d / %{public}@"
+ "en_US_POSIX"
- "%@\n\nPlease fill out the following information to assist with triage:\n\nVehicle Make:\nVehicle Model:\nAdditional Context:"
- "Invalid reader ID"
```
