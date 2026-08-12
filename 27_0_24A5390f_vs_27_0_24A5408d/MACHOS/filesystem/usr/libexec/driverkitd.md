## driverkitd

> `/usr/libexec/driverkitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA.__objc_data`

```diff

-514.0.0.0.0
-  __TEXT.__text: 0xe96bc
-  __TEXT.__auth_stubs: 0x2480
-  __TEXT.__objc_stubs: 0x860
-  __TEXT.__objc_methlist: 0x1f8
-  __TEXT.__objc_classname: 0xb2c
+514.2.1.0.0
+  __TEXT.__text: 0xeba10
+  __TEXT.__auth_stubs: 0x2490
+  __TEXT.__objc_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x224
+  __TEXT.__objc_classname: 0xbac
   __TEXT.__objc_methtype: 0x39a
-  __TEXT.__const: 0xf3f5
+  __TEXT.__const: 0xf485
   __TEXT.__oslogstring: 0x11d9
-  __TEXT.__cstring: 0x8ce4
+  __TEXT.__cstring: 0x9084
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x40bc
-  __TEXT.__swift5_typeref: 0x35f4
+  __TEXT.__constg_swiftt: 0x4130
+  __TEXT.__swift5_typeref: 0x363a
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x2036
-  __TEXT.__swift5_fieldmd: 0x3520
-  __TEXT.__swift5_assocty: 0x468
+  __TEXT.__swift5_reflstr: 0x2056
+  __TEXT.__swift5_fieldmd: 0x3564
+  __TEXT.__swift5_assocty: 0x480
   __TEXT.__swift5_capture: 0x5d8
-  __TEXT.__objc_methname: 0x1346
-  __TEXT.__swift5_proto: 0xc50
-  __TEXT.__swift5_types: 0x3cc
+  __TEXT.__objc_methname: 0x13a6
+  __TEXT.__swift5_proto: 0xc54
+  __TEXT.__swift5_types: 0x3d0
   __TEXT.__swift5_protos: 0xc8
   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__config_plist: 0x641
-  __TEXT.__unwind_info: 0x2740
-  __TEXT.__eh_frame: 0x31ec
-  __DATA_CONST.__const: 0x8950
-  __DATA_CONST.__objc_classlist: 0x1c0
-  __DATA_CONST.__objc_protolist: 0x68
+  __TEXT.__unwind_info: 0x27b0
+  __TEXT.__eh_frame: 0x3374
+  __DATA_CONST.__const: 0x8998
+  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__auth_got: 0x1248
-  __DATA_CONST.__got: 0x508
-  __DATA_CONST.__auth_ptr: 0x850
-  __DATA.__objc_const: 0x3710
-  __DATA.__objc_selrefs: 0x2e8
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__auth_got: 0x1250
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__auth_ptr: 0x858
+  __DATA.__objc_const: 0x3890
+  __DATA.__objc_selrefs: 0x300
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x6290
+  __DATA.__data: 0x63c8
   __DATA.__bss: 0x15360
   __DATA.__common: 0x308
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3610
-  Symbols:   877
-  CStrings:  1205
+  Functions: 3636
+  Symbols:   879
+  CStrings:  1226
 
Symbols:
+ _OBJC_CLASS_$_LSBundleRecord
+ _swift_getObjCClassFromMetadata
CStrings:
+ "App connection from pid %d resolved to an application record with no install session identifier; failing closed"
+ "App server name: %{public}s"
+ "Attempt by unentitled pid %d to access app interface"
+ "Audit token did not resolve to an application record"
+ "Error while getting scoped approval state: %{public}s"
+ "Incoming app request for scoped approval state from pid %d"
+ "KMError while getting scoped approval state: %{public}s"
+ "KernelManagement_executables-514.2.1"
+ "Processing pending requests from the kernel, if any"
+ "Scoped %lu of %lu cached approval entries to install session %{private}s: [%{private}s]"
+ "Unexpected call to applicationRecord(fromAuditToken:)"
+ "_TtC10driverkitd36DriverKitDaemonAppXPCRequestDelegate"
+ "_TtP10driverkitd32DriverKitDaemonAppClientProtocol_"
+ "auditToken"
+ "bundleRecordForAuditToken:error:"
+ "com.apple.DriverKitAppServer"
+ "com.apple.developer.system-extension.install"
+ "com.apple.driverkitd.NSXPCAppRequestSource"
+ "getApprovalStateForCallingAppWithReplyBlock:"
+ "incoming app connection from pid %d"
+ "install session identifier for calling application"
+ "processPendingRequestsOnActivation"
- "KernelManagement_executables-514"
```
