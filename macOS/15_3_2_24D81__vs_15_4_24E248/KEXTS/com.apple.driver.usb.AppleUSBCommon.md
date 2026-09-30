## com.apple.driver.usb.AppleUSBCommon

> `com.apple.driver.usb.AppleUSBCommon`

```diff

-1402.60.3.0.0
+1402.100.21.0.0
   __TEXT.__cstring: 0x301
   __TEXT.__os_log: 0xc6
-  __TEXT_EXEC.__text: 0x57ec
+  __TEXT_EXEC.__text: 0x58e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x110

   __DATA_CONST.__const: 0x1200
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 4BF68B00-45B5-3F3C-9674-56374E4AE0A9
-  Functions: 204
-  Symbols:   422
+  UUID: 1A96AFBC-2827-3E5D-9386-7F16950F2421
+  Functions: 203
+  Symbols:   421
   CStrings:  47
 
Symbols:
- _ZN18AppleUSBDescriptor18initWithDescriptorEPKN11StandardUSB10DescriptorEtht.cold.1
Functions:
~ __ZN19AppleUSBSparseArray16initWithCapacityEjj : 112 -> 116
~ __ZN19AppleUSBSparseArray4freeEv : 144 -> 148
~ __ZN19AppleUSBSparseArray9setObjectEP15OSMetaClassBaseRj : 300 -> 324
~ __ZN19AppleUSBSparseArray12removeObjectEj : 116 -> 124
~ __ZNK19AppleUSBSparseArray24getNextObjectForIteratorEPvPP8OSObject : 124 -> 112
~ __ZN19AppleUSBSparseArray15flushCollectionEv : 120 -> 128
~ __ZN19AppleUSBRequestPool4stopEv : 364 -> 380
~ __ZN19AppleUSBRequestPool4freeEv : 128 -> 132
~ __ZN19AppleUSBRequestPool9gatedStopEv : 140 -> 148
~ __ZN19AppleUSBRequestPool13returnCommandEP9IOCommand : 164 -> 180
~ __ZN19AppleUSBRequestPool18gatedReturnCommandEP9IOCommand : 104 -> 108
~ __ZN19AppleUSBRequestPool10getCommandEb : 280 -> 284
~ __ZN15AppleUSBRequest12initWithPoolEP19AppleUSBRequestPool : 124 -> 128
~ __ZN15AppleUSBRequest4freeEv : 172 -> 176
~ __ZN24AppleUSBRequestCompleter4freeEv : 624 -> 628
~ __ZN24AppleUSBRequestCompleter13onThreadGatedERb : 396 -> 392
~ __ZN24AppleUSBRequestCompleter14enqueueRequestEP15AppleUSBRequest : 1288 -> 1284
~ __ZN24AppleUSBRequestCompleter41completeSynchronousRequestQueueThreadCallEP11thread_call : 344 -> 364
~ __ZN24AppleUSBRequestCompleter46completeSynchronousRequestQueueThreadCallGatedEv : 196 -> 192
~ __ZN24AppleUSBRequestCompleter12checkForWorkEv : 572 -> 584
~ __ZN24AppleUSBRequestCompleter20completeRequestQueueEP11queue_entry : 1972 -> 1984
~ __ZN24AppleUSBRequestCompleter25completeRequestThreadCallEPNS_20tRequestCompleteDataE : 368 -> 388
~ __ZN18AppleUSBDescriptor18initWithDescriptorEPKN11StandardUSB10DescriptorEtht : 212 -> 216
~ __ZN18AppleUSBDescriptor4freeEv : 104 -> 108
~ __ZN23AppleUSBDescriptorCache15descriptorCacheEv : 192 -> 212
~ __ZN23AppleUSBDescriptorCache4initEv : 96 -> 100
~ __ZN23AppleUSBDescriptorCache4freeEv : 272 -> 276
~ __ZN23AppleUSBDescriptorCache13setDescriptorEPKN11StandardUSB10DescriptorEtht : 860 -> 900
~ __ZN23AppleUSBDescriptorCache13getDescriptorEhRtht : 480 -> 496
~ __ZN23AppleUSBDescriptorCache16removeDescriptorEhht : 592 -> 608

```
