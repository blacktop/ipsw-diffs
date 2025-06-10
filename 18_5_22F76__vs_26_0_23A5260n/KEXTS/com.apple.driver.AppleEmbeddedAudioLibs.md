## com.apple.driver.AppleEmbeddedAudioLibs

> `com.apple.driver.AppleEmbeddedAudioLibs`

```diff

-420.3.0.0.0
-  __TEXT.__cstring: 0x1c27
-  __TEXT.__os_log: 0x2c55
-  __TEXT_EXEC.__text: 0xe498
+500.4.0.0.0
+  __TEXT.__cstring: 0x1f41
+  __TEXT.__os_log: 0x2e26
+  __TEXT_EXEC.__text: 0xecb8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1a0
   __DATA.__common: 0xd8

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0xf90
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: 4E44F19F-8757-3E23-AC4B-F2689B24470C
-  Functions: 381
+  UUID: 4F1DC247-B672-32B0-9E85-BA35DFCEFC6A
+  Functions: 393
   Symbols:   0
-  CStrings:  291
+  CStrings:  307
 
CStrings:
+ "!((descriptor.returnData) == nullptr)"
+ "!((inData) == nullptr)"
+ "!((inFunction) == nullptr)"
+ "!((inHostConfig.commandAction) == nullptr)"
+ "!((mHostConfig.commandAction) == nullptr)"
+ "!((outData) == nullptr)"
+ "!((propertyData) == nullptr)"
+ "!((symbol) == nullptr)"
+ "!(inDataSize < descriptor.returnData->getLength())"
+ "!(inDataSize > descriptor.returnData->getLength())"
+ "/Library/Caches/com.apple.xbs/Sources/AppleAudioKextLibs/src/kext/AppleEmbedAudioLibs/AppleAudioDeviceCommandFunction/AudioDeviceCommandFunction.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleAudioKextLibs/src/kext/AppleEmbedAudioLibs/AppleAudioDeviceCommandFunction/AudioDeviceCommandFunctionUtility.cpp"
+ "AudioDeviceCommandFunction::Utility"
+ "inDataSize > 0"
+ "ret = inFunction->processCommand(descriptor) == 0 "
+ "ret = theFunction->validate() == 0 "

```
