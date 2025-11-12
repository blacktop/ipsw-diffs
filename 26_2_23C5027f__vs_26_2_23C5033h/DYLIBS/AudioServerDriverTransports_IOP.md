## AudioServerDriverTransports_IOP

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP`

```diff

-320.1.0.0.0
-  __TEXT.__text: 0xea50
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0xc3c
+320.2.0.0.0
+  __TEXT.__text: 0xef18
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_methlist: 0xc8c
   __TEXT.__gcc_except_tab: 0x13b8
-  __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0xe68
-  __TEXT.__cstring: 0xe58
-  __TEXT.__unwind_info: 0x798
-  __TEXT.__objc_classname: 0x359
-  __TEXT.__objc_methname: 0x1383
-  __TEXT.__objc_methtype: 0x811
-  __TEXT.__objc_stubs: 0x1300
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__const: 0x150
+  __TEXT.__oslogstring: 0xe8a
+  __TEXT.__cstring: 0xe6a
+  __TEXT.__unwind_info: 0x7b8
+  __TEXT.__objc_classname: 0x366
+  __TEXT.__objc_methname: 0x144e
+  __TEXT.__objc_methtype: 0x840
+  __TEXT.__objc_stubs: 0x1480
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x680
+  __DATA_CONST.__objc_selrefs: 0x6e8
   __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x228
-  __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x1748
+  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__objc_const: 0x17d8
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x188
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 37DA98BB-E610-34FB-8ABF-1D6C414BC974
-  Functions: 437
-  Symbols:   1514
-  CStrings:  577
+  UUID: 4F5B850E-6F83-37B3-BB6B-EF5F08F8E071
+  Functions: 445
+  Symbols:   1560
+  CStrings:  599
 
Symbols:
+ +[ASDTBootArgs getBool:]
+ +[ASDTBootArgs getString:]
+ +[ASDTBootArgs getUInt64:]
+ +[ASDTBootArgs get]
+ +[ASDTBootArgs initBootArgsFrom:]
+ +[ASDTBootArgs initBootArgs]
+ +[ASDTBootArgs initBootArgs].cold.1
+ _ASDTBaseLogType
+ _OBJC_CLASS_$_ASDTBootArgs
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_ASDTBootArgs
+ __OBJC_$_CLASS_METHODS_ASDTBootArgs
+ __OBJC_CLASS_RO_$_ASDTBootArgs
+ __OBJC_METACLASS_RO_$_ASDTBootArgs
+ ___19+[ASDTBootArgs get]_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___error
+ _gBootArgs
+ _get.onceToken
+ _objc_enumerationMutation
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$copy
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$dictionary
+ _objc_msgSend$get
+ _objc_msgSend$getString:
+ _objc_msgSend$getUInt64:
+ _objc_msgSend$initBootArgs
+ _objc_msgSend$initBootArgsFrom:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$setObject:forKey:
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _strerror
+ _strtoull
+ _sysctlbyname
CStrings:
+ ""
+ " "
+ "="
+ "ASDTBootArgs"
+ "Failed to load boot args: [%d] %s"
+ "Q24@0:8@16"
+ "componentsSeparatedByString:"
+ "copy"
+ "countByEnumeratingWithState:objects:count:"
+ "dataWithLength:"
+ "dictionary"
+ "get"
+ "getBool:"
+ "getString:"
+ "getUInt64:"
+ "initBootArgs"
+ "initBootArgsFrom:"
+ "kern.bootargs"
+ "objectAtIndex:"
+ "setObject:forKey:"
+ "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"\"{?=\"__ptr_\"^{StatusTracker}}}"
+ "{unique_ptr<ASDT::IOPAudio::ClientManager::UserClient, std::default_delete<ASDT::IOPAudio::ClientManager::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"
+ "{unique_ptr<ASDT::IOPAudio::IOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IOBuffer::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"
+ "{unique_ptr<ASDT::IOPAudio::IsolatedIOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IsolatedIOBuffer::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"
+ "{unique_ptr<ASDT::IOPAudio::LPMic::UserClient, std::default_delete<ASDT::IOPAudio::LPMic::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"
+ "{unique_ptr<ASDT::IOPAudio::VoiceTrigger::UserClient, std::default_delete<ASDT::IOPAudio::VoiceTrigger::UserClient>>=\"\"{?=\"__ptr_\"^{UserClient}}}"
- "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__ptr_\"^{StatusTracker}}"
- "{unique_ptr<ASDT::IOPAudio::ClientManager::UserClient, std::default_delete<ASDT::IOPAudio::ClientManager::UserClient>>=\"__ptr_\"^{UserClient}}"
- "{unique_ptr<ASDT::IOPAudio::IOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IOBuffer::UserClient>>=\"__ptr_\"^{UserClient}}"
- "{unique_ptr<ASDT::IOPAudio::IsolatedIOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IsolatedIOBuffer::UserClient>>=\"__ptr_\"^{UserClient}}"
- "{unique_ptr<ASDT::IOPAudio::LPMic::UserClient, std::default_delete<ASDT::IOPAudio::LPMic::UserClient>>=\"__ptr_\"^{UserClient}}"
- "{unique_ptr<ASDT::IOPAudio::VoiceTrigger::UserClient, std::default_delete<ASDT::IOPAudio::VoiceTrigger::UserClient>>=\"__ptr_\"^{UserClient}}"

```
