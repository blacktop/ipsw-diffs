## com.apple.driver.AppleARMPlatform

> `com.apple.driver.AppleARMPlatform`

```diff

-1150.40.3.0.0
+1150.40.4.0.0
   __TEXT.__const: 0x1ae0
-  __TEXT.__os_log: 0x14f7
-  __TEXT.__cstring: 0xd238
-  __TEXT_EXEC.__text: 0x53894
+  __TEXT.__os_log: 0x1553
+  __TEXT.__cstring: 0xd2a4
+  __TEXT_EXEC.__text: 0x539b4
   __TEXT_EXEC.__auth_stubs: 0xd60
   __DATA.__data: 0x6c8
   __DATA.__common: 0xcd8

   __DATA_CONST.__got: 0x1f8
   Functions: 2238
   Symbols:   0
-  CStrings:  1747
+  CStrings:  1751
 
Functions:
~ __ZN18AppleMCCUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 600 -> 700
~ sub_fffffe000877fe0c -> sub_fffffe000875fe70 : 308 -> 340
~ ____ZN23AppleMemCacheController30getDataCollectionMemDescriptorEv_block_invoke : 248 -> 404
CStrings:
+ "%s:%d: Failed to create mem descriptor for shared data queue\n\n"
+ "%s:%d: No data collection buffer available\n\n"
+ "Failed to create mem descriptor for shared data queue\n"
+ "No data collection buffer available\n"
```
