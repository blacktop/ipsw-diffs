## SystemMigration

> `/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-6164.0.3.0.0
-  __TEXT.__text: 0x100338
-  __TEXT.__objc_methlist: 0x10500
+6164.0.5.0.0
+  __TEXT.__text: 0x1009c0
+  __TEXT.__objc_methlist: 0x10570
   __TEXT.__const: 0x214
-  __TEXT.__gcc_except_tab: 0x38a0
-  __TEXT.__cstring: 0x2324a
+  __TEXT.__gcc_except_tab: 0x3910
+  __TEXT.__cstring: 0x232ca
   __TEXT.__oslogstring: 0x402
   __TEXT.__ustring: 0x147c
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x1a
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x31d0
+  __TEXT.__unwind_info: 0x31f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8300
+  __DATA_CONST.__objc_selrefs: 0x8330
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x4b0
-  __DATA_CONST.__objc_arraydata: 0x6b8
+  __DATA_CONST.__objc_arraydata: 0x6c8
   __DATA_CONST.__got: 0xec0
   __AUTH_CONST.__const: 0x1bd0
-  __AUTH_CONST.__cfstring: 0x19380
-  __AUTH_CONST.__objc_const: 0x16d18
+  __AUTH_CONST.__cfstring: 0x19440
+  __AUTH_CONST.__objc_const: 0x16d78
   __AUTH_CONST.__objc_intobj: 0x690
   __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_dictobj: 0xa0

   __AUTH_CONST.__auth_got: 0x9a8
   __AUTH.__objc_data: 0x3a10
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x1214
-  __DATA.__data: 0x1308
+  __DATA.__objc_ivar: 0x121c
+  __DATA.__data: 0x1310
   __DATA.__bss: 0x158
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5606
-  Symbols:   12983
-  CStrings:  4000
+  Functions: 5617
+  Symbols:   13004
+  CStrings:  4006
 
Symbols:
+ -[SMDCustomize_XPCClientConnection clearCustomizeLatch]
+ -[SMDCustomize_XPCClientConnection dealloc]
+ -[SMDCustomize_XPCClientConnection invalidate]
+ -[SMDCustomize_XPCClientConnection observeValueForKeyPath:ofObject:change:context:]
+ -[SMDCustomize_XPCClientConnection observedSystem]
+ -[SMDCustomize_XPCClientConnection setObservedSystem:]
+ -[SMDPairing_XPCClientConnection invalidate]
+ -[SMPairingManager _startScanning]
+ -[SMPairingManager scanning]
+ -[SMPairingManager setScanning:]
+ OBJC_IVAR_$_SMDCustomize_XPCClientConnection._observedSystem
+ OBJC_IVAR_$_SMPairingManager._scanning
+ ___33-[SMPairingManager startScanning]_block_invoke
+ _kCustomizeSystemStateContext
+ _objc_msgSend$_startScanning
+ _objc_msgSend$clearCustomizeLatch
+ _objc_msgSend$observedSystem
+ _objc_msgSend$scanning
+ _objc_msgSend$setObservedSystem:
+ _objc_msgSend$setScanning:
+ _objc_msgSend$stopScanning
CStrings:
+ "/Data/Library/Caches"
+ "/Data/tmp"
+ "/Library/Caches"
+ "/Users/%@/Library/Containers/"
+ "/Users/%@/Library/Group Containers/"
+ "Library/Metadata/"
```
