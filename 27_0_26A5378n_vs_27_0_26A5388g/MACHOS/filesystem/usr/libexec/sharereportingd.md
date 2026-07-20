## sharereportingd

> `/usr/libexec/sharereportingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-94.0.0.0.0
-  __TEXT.__text: 0x44cbc
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__objc_stubs: 0x7c0
+96.0.0.0.0
+  __TEXT.__text: 0x451d8
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x2e4
-  __TEXT.__const: 0x3a68
-  __TEXT.__swift5_typeref: 0xbbd
+  __TEXT.__const: 0x3a48
+  __TEXT.__swift5_typeref: 0xc2d
   __TEXT.__swift5_capture: 0x424
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x2a17
+  __TEXT.__cstring: 0x2a67
   __TEXT.__constg_swiftt: 0xc2c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x8e3
-  __TEXT.__swift5_fieldmd: 0xdec
+  __TEXT.__swift5_reflstr: 0x8d3
+  __TEXT.__swift5_fieldmd: 0xdd4
   __TEXT.__swift5_types: 0xf0
   __TEXT.__swift_as_entry: 0xe0
   __TEXT.__swift_as_ret: 0x1ac
   __TEXT.__swift_as_cont: 0x290
-  __TEXT.__objc_methname: 0x85e
+  __TEXT.__objc_methname: 0x84e
   __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__swift5_proto: 0x2b4
   __TEXT.__oslogstring: 0x34

   __TEXT.__objc_methtype: 0x307
   __TEXT.__unwind_info: 0x1498
   __TEXT.__eh_frame: 0x3750
-  __DATA_CONST.__const: 0x28f0
+  __DATA_CONST.__const: 0x28d8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0x8d0
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__auth_ptr: 0x330
+  __DATA_CONST.__auth_got: 0x900
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__auth_ptr: 0x340
   __DATA.__objc_const: 0x8a8
-  __DATA.__objc_selrefs: 0x2f8
+  __DATA.__objc_selrefs: 0x2f0
   __DATA.__objc_data: 0x3d0
-  __DATA.__data: 0x17f0
+  __DATA.__data: 0x1830
   __DATA.__common: 0xb0
-  __DATA.__bss: 0x5480
+  __DATA.__bss: 0x5490
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1406
-  Symbols:   449
+  Functions: 1401
+  Symbols:   458
   CStrings:  384
 
Symbols:
+ _$s17_StringProcessing14RegexComponentP5regexAA0C0Vy0C6OutputQzGvgTj
+ _$s17_StringProcessing5RegexV06_regexA07versionACyxGSS_SitcfC
+ _$s17_StringProcessing5RegexV10wholeMatch2inAC0E0Vyx_GSgSs_tKF
+ _$s17_StringProcessing5RegexV5MatchV13dynamicMemberqd__s7KeyPathCyxqd__G_tcluig
+ _$s17_StringProcessing5RegexV5MatchVMn
+ _$s17_StringProcessing5RegexVMn
+ _$s17_StringProcessing5RegexVyxGAA0C9ComponentAAMc
+ _$sSS14_fromSubstringySSSshFZ
+ _$sSSySsSnySS5IndexVGcig
+ _swift_getKeyPath
- _$s10Foundation3URLV36_unconditionallyBridgeFromObjectiveCyACSo5NSURLCSgFZ
CStrings:
+ "#/https://www\\.icloud\\.com/[^/]+/(?<identifier>[^#]+)(#.*)?/#"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/TrustKit/Source/BackgroundActivityManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/TrustKit/Source/CoreAnalyticsManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/TrustKit/Source/GenericSQLiteManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/TrustKit/Source/SQLiteBindingHelpers.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/TrustKit/Source/SQLiteColumnExtractor.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/TrustKit/Source/Utility/ContainerManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/sharereportingd/CleanUpBackgroundActivity.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/sharereportingd/Server.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/sharereportingd/ServerProxy.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/sharereportingd/ShareReportManager+Types.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/sharereportingd/ShareReportManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.zlam2q/Sources/TrustKit/sharereportingd/main.swift"
+ "https://www.icloud.com/share/"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/TrustKit/Source/BackgroundActivityManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/TrustKit/Source/CoreAnalyticsManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/TrustKit/Source/GenericSQLiteManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/TrustKit/Source/SQLiteBindingHelpers.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/TrustKit/Source/SQLiteColumnExtractor.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/TrustKit/Source/Utility/ContainerManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/sharereportingd/CleanUpBackgroundActivity.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/sharereportingd/Server.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/sharereportingd/ServerProxy.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/sharereportingd/ShareReportManager+Types.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/sharereportingd/ShareReportManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ltXv5W/Sources/TrustKit/sharereportingd/main.swift"
- "asset-file-url"
- "fileURL"
```
