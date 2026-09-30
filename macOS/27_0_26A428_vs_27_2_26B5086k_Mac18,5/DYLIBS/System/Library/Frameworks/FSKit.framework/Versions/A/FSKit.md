## FSKit

> `/System/Library/Frameworks/FSKit.framework/Versions/A/FSKit`

```diff

-974.0.13.0.2
-  __TEXT.__text: 0x57854
-  __TEXT.__objc_methlist: 0x6348
+974.40.11.0.0
+  __TEXT.__text: 0x57af0
+  __TEXT.__objc_methlist: 0x6378
   __TEXT.__const: 0x4a8
-  __TEXT.__gcc_except_tab: 0xe7c
-  __TEXT.__oslogstring: 0x3fc6
-  __TEXT.__cstring: 0x636f
+  __TEXT.__gcc_except_tab: 0xe84
+  __TEXT.__oslogstring: 0x4006
+  __TEXT.__cstring: 0x63df
   __TEXT.__swift5_typeref: 0x264
   __TEXT.__swift5_capture: 0xec
   __TEXT.__swift_as_entry: 0x1c

   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x22b8
+  __TEXT.__unwind_info: 0x22c8
   __TEXT.__eh_frame: 0x400
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x278
   __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c28
-  __DATA_CONST.__objc_protorefs: 0x148
+  __DATA_CONST.__objc_selrefs: 0x2c40
+  __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x488
   __DATA_CONST.__got: 0x488
   __AUTH_CONST.__const: 0x1ec0
-  __AUTH_CONST.__cfstring: 0x2b20
-  __AUTH_CONST.__objc_const: 0xb2b8
+  __AUTH_CONST.__cfstring: 0x2b40
+  __AUTH_CONST.__objc_const: 0xb2e8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__auth_got: 0x7e0
-  __AUTH.__objc_data: 0x1b38
-  __AUTH.__data: 0x58
+  __AUTH.__objc_data: 0x1fe0
+  __AUTH.__data: 0x80
   __DATA.__objc_ivar: 0x640
-  __DATA.__data: 0x1538
-  __DATA_DIRTY.__objc_data: 0x9f8
-  __DATA_DIRTY.__data: 0x80
-  __DATA_DIRTY.__bss: 0x110
-  __DATA_DIRTY.__common: 0x18
+  __DATA.__data: 0x15c8
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x550
+  __DATA_DIRTY.__data: 0x20
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2750
-  Symbols:   5223
-  CStrings:  1089
+  Functions: 2754
+  Symbols:   5237
+  CStrings:  1094
 
Symbols:
+ +[FSKitConstants(project) FSClientFSCKXPCProtocols]
+ -[FSClient hasFSCKEntitlement]
+ -[FSClient isEntitlementSet:]
+ GCC_except_table109
+ GCC_except_table114
+ GCC_except_table20
+ GCC_except_table44
+ GCC_except_table52
+ GCC_except_table79
+ GCC_except_table8
+ GCC_except_table84
+ GCC_except_table91
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FSClientFSCKXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FSClientFSCKXPC
+ __OBJC_$_PROTOCOL_REFS_FSClientFSCKXPC
+ __OBJC_LABEL_PROTOCOL_$_FSClientFSCKXPC
+ __OBJC_PROTOCOL_$_FSClientFSCKXPC
+ __OBJC_PROTOCOL_REFERENCE_$_FSClientFSCKXPC
+ _objc_msgSend$FSClientFSCKXPCProtocols
+ _objc_msgSend$hasFSCKEntitlement
+ _objc_msgSend$isEntitlementSet:
- GCC_except_table107
- GCC_except_table112
- GCC_except_table42
- GCC_except_table5
- GCC_except_table50
- GCC_except_table82
- GCC_except_table89
CStrings:
+ "%s: rename flags aren't supported (requested 0x%x). Error = %d."
+ "FSClient setting up %s connection to fskitd"
+ "com.apple.private.security.disk-device-access"
+ "com.apple.rootless.restricted-block-devices"
+ "fsck"
+ "unprivileged"
- "FSClient setting up %@ connection to fskitd"
```
