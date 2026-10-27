## com.apple.driver.CoreStorage

> `com.apple.driver.CoreStorage`

```diff

-572.0.0.0.0
+572.40.2.0.1
   __TEXT.__const: 0x728
-  __TEXT.__cstring: 0x8b44
-  __TEXT_EXEC.__text: 0x9a100
-  __TEXT_EXEC.__auth_stubs: 0xf00
+  __TEXT.__cstring: 0x8bad
+  __TEXT_EXEC.__text: 0x9a24c
+  __TEXT_EXEC.__auth_stubs: 0xf10
   __DATA.__data: 0x870
   __DATA.__common: 0x3e0
   __DATA.__bss: 0x28

   __DATA_CONST.__const: 0x6880
   __DATA_CONST.__kalloc_type: 0x340
   __DATA_CONST.__kalloc_var: 0xa50
-  __DATA_CONST.__auth_got: 0x780
+  __DATA_CONST.__auth_got: 0x788
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__auth_ptr: 0x10
   Functions: 1737
-  Symbols:   2602
-  CStrings:  981
+  Symbols:   2603
+  CStrings:  985
 
Symbols:
+ _csr_check
Functions:
~ __ZN19CoreStoragePhysical4initEP12OSDictionary : 184 -> 180
~ __ZN19CoreStoragePhysical5startEP9IOService : 1540 -> 1556
~ __ZN19CoreStoragePhysical10readHeaderEv : 2084 -> 2404
CStrings:
+ "Physical Interconnect"
+ "Protocol Characteristics"
+ "Virtual Interface"
+ "com.apple.corestorage.pv.blockDiskImage"
```
