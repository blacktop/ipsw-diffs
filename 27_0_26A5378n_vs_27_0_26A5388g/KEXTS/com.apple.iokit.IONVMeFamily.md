## com.apple.iokit.IONVMeFamily

> `com.apple.iokit.IONVMeFamily`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-877.0.3.0.0
+877.0.6.0.0
   __TEXT.__cstring: 0x109cd
   __TEXT.__const: 0x740
-  __TEXT_EXEC.__text: 0x5e660
+  __TEXT_EXEC.__text: 0x5e6ac
   __TEXT_EXEC.__auth_stubs: 0xe00
   __DATA.__data: 0x46c
   __DATA.__common: 0x578
Functions:
~ __ZN23AppleANS2NVMeController20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 660 -> 672
~ __ZN23AppleANS2NVMeController17PPMArrivalHandlerEPvP9IOServiceP10IONotifier : 456 -> 520
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/AppleNVMeBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/AppleNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/AppleNVMeRequest.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/AppleNVMeRequestPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/AppleNVMeRequestPoolTagReserve.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/AppleNVMeRequestTimer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/AppleNVMeSMARTUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/AppleNVMeUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/AppleNVMeWorkLoop.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/IONVMeBlockStorageDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/IONVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Common/IONVMeControllerPolledAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleANS2CGNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleANS2CGv2Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleANS2DARTNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleANS2NVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleANS3CGv2Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleANS3NVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeDiagnostics.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeNVRAM.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeTemperatureSensor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleNVMeEAN.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleNVMeEANUC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceUC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceUC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/AppleNVMeUpdateUC.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/IOEmbeddedNVMeBlockDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/IONVMeEffaceableDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/IONVMeLifeboatBlockDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mGoG5J/Sources/IONVMeFamily/Embedded/NVMeSEPNotifier.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeRequest.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeRequestPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeRequestPoolTagReserve.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeRequestTimer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeSMARTUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/AppleNVMeWorkLoop.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/IONVMeBlockStorageDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/IONVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Common/IONVMeControllerPolledAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS2CGNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS2CGv2Controller.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS2DARTNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS2NVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS3CGv2Controller.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleANS3NVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeDiagnostics.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeNVRAM.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeTemperatureSensor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeEAN.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeEANUC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeFWNamespaceUC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceUC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/AppleNVMeUpdateUC.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/IOEmbeddedNVMeBlockDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/IONVMeEffaceableDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/IONVMeLifeboatBlockDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QcoIek/Sources/IONVMeFamily/Embedded/NVMeSEPNotifier.cpp"
```
