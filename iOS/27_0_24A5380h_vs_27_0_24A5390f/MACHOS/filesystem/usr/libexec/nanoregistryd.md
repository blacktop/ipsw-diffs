## nanoregistryd

> `/usr/libexec/nanoregistryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1075.1.0.0.0
-  __TEXT.__text: 0x100628
+1075.1.1.0.0
+  __TEXT.__text: 0x1006b4
   __TEXT.__auth_stubs: 0x1100
   __TEXT.__objc_stubs: 0x10fe0
   __TEXT.__objc_methlist: 0xdad4
   __TEXT.__const: 0x69a
   __TEXT.__gcc_except_tab: 0x1cd8
   __TEXT.__objc_methname: 0x1c5ee
-  __TEXT.__cstring: 0xe0aa
-  __TEXT.__oslogstring: 0x16191
+  __TEXT.__cstring: 0xe0ac
+  __TEXT.__oslogstring: 0x16281
   __TEXT.__objc_classname: 0x21b9
   __TEXT.__objc_methtype: 0x4bc9
   __TEXT.__dlopen_cstrs: 0xef

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x210
   __DATA_CONST.__auth_got: 0x890
-  __DATA_CONST.__got: 0xc90
+  __DATA_CONST.__got: 0xdc8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x1a380
   __DATA.__objc_selrefs: 0x5e88

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5827
+  Functions: 5828
   Symbols:   705
-  CStrings:  8651
+  CStrings:  8652
 
Functions:
~ sub_100061644 : 660 -> 732
+ sub_1000fd968
CStrings:
+ "72"
+ "BLOCKSYNCTESTMODE ENABLED: EPSagaTransactionPairedSync paired sync disabled because internal default blockSyncTestMode (com.apple.NanoRegistry) is set; skipping initial sync and not posting NRInitialPairedSyncDidCompleteDarwinNotification."
+ "NanoRegistry-1075.1.1"
- "55"
- "NanoRegistry-1075.1"
```
