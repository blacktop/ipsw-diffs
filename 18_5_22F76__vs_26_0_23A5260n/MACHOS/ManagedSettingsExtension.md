## ManagedSettingsExtension

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension`

```diff

-2400.5.2.0.0
-  __TEXT.__text: 0x1eccc
-  __TEXT.__auth_stubs: 0x900
+2420.1.1.0.0
+  __TEXT.__text: 0x1bbfc
+  __TEXT.__auth_stubs: 0x8d0
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__objc_methlist: 0x5cc
+  __TEXT.__objc_methlist: 0x60c
   __TEXT.__objc_classname: 0x8d
-  __TEXT.__objc_methname: 0x1ba0
-  __TEXT.__objc_methtype: 0x241
-  __TEXT.__const: 0xd58
-  __TEXT.__constg_swiftt: 0xc28
-  __TEXT.__swift5_typeref: 0x810
+  __TEXT.__objc_methname: 0x1c8a
+  __TEXT.__objc_methtype: 0x217
+  __TEXT.__const: 0x10a8
+  __TEXT.__constg_swiftt: 0xd88
+  __TEXT.__swift5_typeref: 0x864
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x1b3
-  __TEXT.__swift5_fieldmd: 0x568
-  __TEXT.__swift5_types: 0x84
-  __TEXT.__cstring: 0x1892
-  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__swift5_reflstr: 0x9c3
+  __TEXT.__swift5_fieldmd: 0x914
+  __TEXT.__swift5_types: 0xac
+  __TEXT.__cstring: 0x19a2
+  __TEXT.__swift5_proto: 0x84
   __TEXT.__swift5_protos: 0x70
-  __TEXT.__oslogstring: 0x20bd
+  __TEXT.__oslogstring: 0x216d
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x318
   __TEXT.__eh_frame: 0x110
-  __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0x4f0
-  __DATA_CONST.__auth_ptr: 0x1d0
-  __DATA_CONST.__const: 0xc40
+  __DATA_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x520
+  __DATA_CONST.__auth_ptr: 0x1b8
+  __DATA_CONST.__const: 0x1218
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x990
-  __DATA.__objc_selrefs: 0x9a8
+  __DATA.__objc_const: 0x9e0
+  __DATA.__objc_selrefs: 0xa30
   __DATA.__objc_data: 0x170
-  __DATA.__data: 0x390
+  __DATA.__data: 0x420
   __DATA.__common: 0x40
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ManagedSettings.framework/ManagedSettings

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: A31F329A-5560-352A-A079-17EF1721569D
-  Functions: 429
-  Symbols:   258
-  CStrings:  610
+  UUID: 0C019F4B-942F-3A2A-85E2-363EED422A0D
+  Functions: 493
+  Symbols:   260
+  CStrings:  638
 
Symbols:
+ _MCFeatureMediaPurchaseAllowed
+ _MCFeatureSafariFraudWarningForced
+ _MCFeatureSafariJavaScriptAllowed
+ _MCFeatureSafariPopUpsAllowed
+ _MCFeatureSafariSummaryAllowed
+ _OBJC_CLASS_$_IXApplicationIdentity
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_checkMetadataState
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_release_n
CStrings:
+ " onlyAllowBookmarks: "
+ "Applied %{public}s"
+ "Applying denyJavaScript settings: %{bool}d, privacy: .public)"
+ "Applying denyMediaPurchase setting: %{bool,public}d"
+ "Applying denyPopups settings: %{bool}d, privacy: .public)"
+ "Applying denySummary settings: %{bool}d, privacy: .public)"
+ "Applying forceFraudWarning settings: %{bool}d, privacy: .public)"
+ "B52@0:8@\"NSDictionary\"16B24@\"NSString\"28@\"NSString\"36^@44"
+ "B52@0:8@16B24@28@36^@44"
+ "Removed %{public}s restrictions"
+ "applyRestrictionDictionary:toSystem:clientType:clientUUID:outError:"
+ "bookmark"
+ "denyJavaScript"
+ "denyJavaScriptMetadata"
+ "denyMediaPurchase"
+ "denyMediaPurchaseMetadata"
+ "denyPopups"
+ "denyPopupsMetadata"
+ "denySummary"
+ "denySummaryMetadata"
+ "effectiveDenyJavaScript should never be nil"
+ "effectiveDenyMediaPurchase should never be nil"
+ "effectiveDenyPopups should never be nil"
+ "effectiveDenySummary should never be nil"
+ "effectiveForceFraudWarning should never be nil"
+ "forceFraudWarning"
+ "forceFraudWarningMetadata"
+ "initWithBundleID:"
+ "mediaPurchaseAllowed"
+ "safariFraudWarningForced"
+ "safariJavaScriptAllowed"
+ "safariPopUpsAllowed"
+ "safariSummaryAllowed"
+ "setRemovability:forAppWithIdentity:byClient:completion:"
- "Applied %{public}s restrictions, restrictionChanged=%{public}s effectiveSettingsChanged=%{public}s"
- "B80@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48^B56^B64^@72"
- "B80@0:8@16@24@32@40@48^B56^B64^@72"
- "Removed %{public}s restrictions, restrictionChanged=%{public}s effectiveSettingsChanged=%{public}s"
- "applyRestrictionDictionary:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:"
- "setRemovability:forAppWithBundleID:byClient:completion:"

```
