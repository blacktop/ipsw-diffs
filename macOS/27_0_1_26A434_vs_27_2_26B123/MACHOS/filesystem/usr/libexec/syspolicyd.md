## syspolicyd

> `/usr/libexec/syspolicyd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__info_plist`
- `__TEXT.__dof_security_`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-823.1.1.0.0
-  __TEXT.__text: 0xb0590
-  __TEXT.__auth_stubs: 0x2c50
-  __TEXT.__objc_stubs: 0xa5e0
+823.40.13.0.0
+  __TEXT.__text: 0xb15f4
+  __TEXT.__auth_stubs: 0x2c60
+  __TEXT.__objc_stubs: 0xa6c0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x53bc
+  __TEXT.__objc_methlist: 0x53dc
   __TEXT.__const: 0x1ff8
-  __TEXT.__objc_methname: 0xd1f1
-  __TEXT.__cstring: 0x11bb3
+  __TEXT.__objc_methname: 0xd31a
+  __TEXT.__cstring: 0x11c43
   __TEXT.__objc_classname: 0x838
-  __TEXT.__objc_methtype: 0x280b
-  __TEXT.__oslogstring: 0xa0d6
-  __TEXT.__gcc_except_tab: 0x1c20
+  __TEXT.__objc_methtype: 0x2800
+  __TEXT.__oslogstring: 0xa336
+  __TEXT.__gcc_except_tab: 0x1c80
   __TEXT.__swift5_typeref: 0x410
   __TEXT.__swift5_capture: 0x1b4
   __TEXT.__constg_swiftt: 0x4a0

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__info_plist: 0x3b5
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x33d0
+  __TEXT.__unwind_info: 0x3410
   __TEXT.__eh_frame: 0x1b8
   __DATA_CONST.__const: 0x3c98
-  __DATA_CONST.__cfstring: 0x8d00
+  __DATA_CONST.__cfstring: 0x8e40
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_arraydata: 0x5a8
   __DATA_CONST.__objc_arrayobj: 0x2a0
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1640
+  __DATA_CONST.__auth_got: 0x1648
   __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x208
-  __DATA.__objc_const: 0x9f70
-  __DATA.__objc_selrefs: 0x2f20
-  __DATA.__objc_ivar: 0x814
+  __DATA.__objc_const: 0x9fb8
+  __DATA.__objc_selrefs: 0x2f58
+  __DATA.__objc_ivar: 0x81c
   __DATA.__objc_data: 0x2208
   __DATA.__data: 0xdb2
-  __DATA.__bss: 0xad0
+  __DATA.__bss: 0xac0
   __DATA.__common: 0x3c0
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3593
-  Symbols:   1065
-  CStrings:  5570
+  Functions: 3611
+  Symbols:   1066
+  CStrings:  5605
 
Symbols:
+ __CFBundleFlushBundleCaches
CStrings:
+ "Absent"
+ "Clean"
+ "DurationMs"
+ "Errno(%d)"
+ "Failed bundle integrity check: %d, %d"
+ "Failed to get the path of a file handle: %s"
+ "Failed to stat file handle: %s"
+ "Failed to stat target: %s error: %s"
+ "Failed to stat the path of a file handle (%s): %s"
+ "File handle has no usable descriptor"
+ "File handle is not a regular file: mode %o"
+ "File handle is not usable: %@"
+ "HashLength"
+ "HashType"
+ "Invalid script file handle"
+ "Online"
+ "Path of a file handle (%s) no longer refers to the open file"
+ "Refusing script scan: unusable script file handle"
+ "Result"
+ "Target identity is not verified on %s: %s"
+ "Target identity mismatch, refusing to act on it: %@"
+ "Target is not the object that was scanned: (%d,%llu) != (%d,%llu), %s"
+ "Unable to open %@ to refresh its localizations."
+ "Unable to open target: %d, %s"
+ "Unable to stat target: %d, %s"
+ "Unable to unregister app bundle: %d, %d"
+ "_objectDev"
+ "_objectIno"
+ "bundleURL"
+ "com.apple.syspolicy.Gatekeeper.RevocationLookup"
+ "fileDescriptor"
+ "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
+ "getScriptScanEvaluationForFileHandle:scriptHash:scanResult:withReply:"
+ "i24@0:8^i16"
+ "openVerifiedDescriptorWithError:"
+ "reason"
+ "reportTargetIdentityMismatch:"
+ "sendTicketLookupWithHashLength:withHashType:wasOnline:withResult:withDurationMs:"
+ "v44@0:8Q16I24B28i32d36"
+ "v48@0:8@\"NSFileHandle\"16@\"NSString\"24@\"XProtectScanResult\"32@?<v@?@\"SPScriptScanEvaluation\"@\"NSError\">40"
- "Failed bundle integrity check: %d, %@"
- "Unable to open app for integrity check: %d, %@"
- "Unable to unregister app bundle: %d, %@"
- "getScriptScanEvaluationFor:scriptHash:scanResult:withReply:"
- "v48@0:8@\"NSURL\"16@\"NSString\"24@\"XProtectScanResult\"32@?<v@?@\"SPScriptScanEvaluation\"@\"NSError\">40"
```
