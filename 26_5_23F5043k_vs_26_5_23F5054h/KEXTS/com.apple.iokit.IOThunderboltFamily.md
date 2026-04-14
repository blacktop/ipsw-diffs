## com.apple.iokit.IOThunderboltFamily

> `com.apple.iokit.IOThunderboltFamily`

```diff

-6805.100.15.0.0
-  __TEXT.__cstring: 0x49e4a
-  __TEXT.__os_log: 0x3aee7
+6805.120.2.0.0
+  __TEXT.__cstring: 0x49f28
+  __TEXT.__os_log: 0x3afb3
   __TEXT.__const: 0xb60
-  __TEXT_EXEC.__text: 0x1c3f1c
+  __TEXT_EXEC.__text: 0x1c4390
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb22
   __DATA.__common: 0x15b0

   __DATA_CONST.__const: 0x23e18
   __DATA_CONST.__kalloc_type: 0x22c0
   __DATA_CONST.__kalloc_var: 0xbe0
-  UUID: 1A28123F-C482-30F7-A9AF-3F8AF9501C83
+  UUID: 70F6DCCE-4B56-3131-8875-65A635CF451F
   Functions: 5586
   Symbols:   0
-  CStrings:  6107
+  CStrings:  6112
 
Functions:
~ __ZN33IOThunderboltXDomainServiceClient15initWithServiceEP27IOThunderboltXDomainService : 2264 -> 2312
~ __ZN22IOThunderboltLocalNode16publishXDServiceEPcjjjj : 1852 -> 1880
~ sub_fffffe000a09993c -> sub_fffffe000a09ea88 : 292 -> 340
~ __ZN22IOThunderboltLocalNode34publishXDServiceDictionaryInternalEPcP12OSDictionaryb : 9540 -> 9824
~ __ZN27IOThunderboltXDomainService20setXDomainPropertiesEP9IOServiceP34IOThunderboltXDPropertiesDirectory : 1632 -> 1744
~ sub_fffffe000a0ad18c -> sub_fffffe000a0b2494 : 376 -> 304
~ sub_fffffe000a0b1a30 -> sub_fffffe000a0b6cf0 : 92 -> 112
~ __ZN35IOThunderboltXDLocalPropertiesCache16encodeDictionaryEP12OSDictionary : 13500 -> 14128
~ __ZN35IOThunderboltXDLocalPropertiesCache24addDictionaryToWorkQueueEP12OSDictionaryP8OSNumberP7OSArray : 2752 -> 2784
~ __ZN24IOThunderboltXDDirectory8addEntryEPKc11OSSharedPtrI8OSObjectE : 760 -> 748
~ ____ZN40IOThunderboltXDomainServiceClientManager15publishServicesEv_block_invoke : 1824 -> 1848
CStrings:
+ "%lldus IOThunderboltLocalNode<%p>::publishXDServiceDictionary - Creating new root directory\n"
+ "%lldus IOThunderboltXDLocalPropertiesCache<%p>::encodeDictionary - entry key string '%s' key value 0x%016llx \n"
+ "21:36:39"
+ "Apr  5 2026"
+ "Service Key Value"
- "18:33:50"
- "Mar 20 2026"

```
