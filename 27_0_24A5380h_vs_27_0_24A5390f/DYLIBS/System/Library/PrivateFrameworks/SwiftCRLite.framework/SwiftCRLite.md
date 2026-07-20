## SwiftCRLite

> `/System/Library/PrivateFrameworks/SwiftCRLite.framework/SwiftCRLite`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-134.0.15.0.0
-  __TEXT.__text: 0xb57c4
-  __TEXT.__objc_methlist: 0x4bc
-  __TEXT.__const: 0x9254
-  __TEXT.__cstring: 0x40bc
-  __TEXT.__oslogstring: 0x17fe
+134.0.18.0.0
+  __TEXT.__text: 0xb646c
+  __TEXT.__objc_methlist: 0x53c
+  __TEXT.__const: 0x924c
+  __TEXT.__cstring: 0x40fc
+  __TEXT.__oslogstring: 0x181e
   __TEXT.__swift5_typeref: 0x1e97
   __TEXT.__swift5_reflstr: 0x1e15
   __TEXT.__swift5_assocty: 0x3b0
-  __TEXT.__constg_swiftt: 0x1be4
+  __TEXT.__constg_swiftt: 0x1bec
   __TEXT.__swift5_fieldmd: 0x2bd8
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_proto: 0x6cc

   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift_as_cont: 0xa8
   __TEXT.__swift5_mpenum: 0x94
-  __TEXT.__unwind_info: 0x2638
+  __TEXT.__unwind_info: 0x2648
   __TEXT.__eh_frame: 0x5024
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x148
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x458
+  __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0x578
   __AUTH_CONST.__const: 0x5cb1
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x1820
-  __AUTH_CONST.__auth_got: 0x1208
-  __AUTH.__objc_data: 0x90
+  __AUTH_CONST.__objc_const: 0x19e0
+  __AUTH_CONST.__auth_got: 0x1220
+  __AUTH.__objc_data: 0xe0
   __AUTH.__data: 0x308
-  __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x11b8
+  __DATA.__objc_ivar: 0x28
+  __DATA.__data: 0x11c8
   __DATA.__bss: 0xac10
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x690
+  __DATA.__common: 0x20
+  __DATA_DIRTY.__objc_data: 0x698
   __DATA_DIRTY.__data: 0x2008
   __DATA_DIRTY.__bss: 0x2980
   __DATA_DIRTY.__common: 0xc0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3384
-  Symbols:   1412
-  CStrings:  539
+  Functions: 3400
+  Symbols:   1440
+  CStrings:  543
 
Symbols:
+ -[SwiftCRLiteClient findValidInfoForCertificate:issuer:]
+ -[SwiftValidInfo .cxx_destruct]
+ -[SwiftValidInfo flags]
+ -[SwiftValidInfo format]
+ -[SwiftValidInfo initWithFormat:flags:matched:notBeforeDate:notAfterDate:policyConstraints:]
+ -[SwiftValidInfo matched]
+ -[SwiftValidInfo notAfterDate]
+ -[SwiftValidInfo notBeforeDate]
+ -[SwiftValidInfo policyConstraints]
+ _CFBooleanGetTypeID
+ _CFGetTypeID
+ _OBJC_CLASS_$_SwiftValidInfo
+ _OBJC_IVAR_$_SwiftValidInfo._flags
+ _OBJC_IVAR_$_SwiftValidInfo._format
+ _OBJC_IVAR_$_SwiftValidInfo._matched
+ _OBJC_IVAR_$_SwiftValidInfo._notAfterDate
+ _OBJC_IVAR_$_SwiftValidInfo._notBeforeDate
+ _OBJC_IVAR_$_SwiftValidInfo._policyConstraints
+ _OBJC_METACLASS_$_SwiftValidInfo
+ __OBJC_$_INSTANCE_METHODS_SwiftValidInfo
+ __OBJC_$_INSTANCE_VARIABLES_SwiftValidInfo
+ __OBJC_$_PROP_LIST_SwiftValidInfo
+ __OBJC_CLASS_RO_$_SwiftValidInfo
+ __OBJC_METACLASS_RO_$_SwiftValidInfo
+ _kCFPreferencesCurrentHost
+ _objc_msgSend$findValidInfoForCertificate:issuerCert:error:
+ _objc_msgSend$initWithFormat:flags:matched:notBeforeDate:notAfterDate:policyConstraints:
+ _swift_unknownObjectRelease_n
CStrings:
+ "3"
+ "ValidUpdateBackground"
+ "chmod 0o644 %s failed: %s"
+ "com.apple.security"
```
