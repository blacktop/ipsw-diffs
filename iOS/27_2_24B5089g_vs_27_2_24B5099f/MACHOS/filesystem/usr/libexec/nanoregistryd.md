## nanoregistryd

> `/usr/libexec/nanoregistryd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1075.12.0.0.0
-  __TEXT.__text: 0xfd834
-  __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_stubs: 0x110a0
-  __TEXT.__objc_methlist: 0xdb14
-  __TEXT.__const: 0x6aa
+1075.15.0.0.0
+  __TEXT.__text: 0xfe340
+  __TEXT.__auth_stubs: 0x1140
+  __TEXT.__objc_stubs: 0x110e0
+  __TEXT.__objc_methlist: 0xdbec
+  __TEXT.__const: 0x69a
   __TEXT.__gcc_except_tab: 0x1d30
-  __TEXT.__objc_methname: 0x1c7f1
-  __TEXT.__cstring: 0xe274
-  __TEXT.__oslogstring: 0x16513
-  __TEXT.__objc_classname: 0x21b9
+  __TEXT.__objc_methname: 0x1c853
+  __TEXT.__cstring: 0xe2cb
+  __TEXT.__oslogstring: 0x16612
+  __TEXT.__objc_classname: 0x21fc
   __TEXT.__objc_methtype: 0x4be2
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x4868
-  __DATA_CONST.__const: 0x4c20
-  __DATA_CONST.__cfstring: 0xc200
-  __DATA_CONST.__objc_classlist: 0x7e8
+  __TEXT.__unwind_info: 0x48a0
+  __DATA_CONST.__const: 0x4c38
+  __DATA_CONST.__cfstring: 0xc280
+  __DATA_CONST.__objc_classlist: 0x7f8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x478
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x210
-  __DATA_CONST.__auth_got: 0x8a0
+  __DATA_CONST.__auth_got: 0x8b0
   __DATA_CONST.__got: 0xdd0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x1a400
-  __DATA.__objc_selrefs: 0x5ec0
-  __DATA.__objc_ivar: 0x11ec
-  __DATA.__objc_data: 0x4f10
+  __DATA.__objc_const: 0x1a688
+  __DATA.__objc_selrefs: 0x5ed8
+  __DATA.__objc_ivar: 0x11f4
+  __DATA.__objc_data: 0x4fb0
   __DATA.__data: 0x19e0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5834
-  Symbols:   708
-  CStrings:  8679
+  Functions: 5853
+  Symbols:   710
+  CStrings:  8691
 
Symbols:
+ _CFPreferencesCopyKeyList
+ _CFPreferencesSynchronize
CStrings:
+ "39"
+ "EPSagaOperandStringArray"
+ "EPSagaTransactionEraseUserDefaultsDomains"
+ "EPSagaTransactionEraseUserDefaultsDomains: cleared %ld key(s) from %@, error=%@"
+ "EPSagaTransactionEraseUserDefaultsDomains: could not resolve %@ for %{public}@, skipping"
+ "EPSagaTransactionEraseUserDefaultsDomains: erased %ld key(s) from %@, synchronized=%d"
+ "NanoRegistry-1075.15"
+ "T@\"NSArray\",R,N,V_strings"
+ "copyKeyList"
+ "initWithDomain:pairingID:pairingDataStore:"
+ "initWithStrings:"
+ "localPairingDataStorePath"
+ "npsPerGizmoDomainsToClear"
+ "userDefaultsDomainsToErase"
- "42"
- "NanoRegistry-1075.12"
```
