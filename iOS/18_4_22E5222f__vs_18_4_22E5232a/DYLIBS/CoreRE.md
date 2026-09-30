## CoreRE

> `/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE`

```diff

-366.100.10.0.1
-  __TEXT.__text: 0x120faa8
+366.100.14.0.0
+  __TEXT.__text: 0x12105c8
   __TEXT.__auth_stubs: 0x6640
-  __TEXT.__objc_methlist: 0x3ad0
+  __TEXT.__objc_methlist: 0x3ae8
   __TEXT.__const: 0xcf3c0
-  __TEXT.__cstring: 0x8e07e
+  __TEXT.__cstring: 0x8e096
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0xc6b0
-  __TEXT.__oslogstring: 0x3bf89
+  __TEXT.__gcc_except_tab: 0xc78c
+  __TEXT.__oslogstring: 0x3c2fa
   __TEXT.__ustring: 0x1a
-  __TEXT.__unwind_info: 0x5558
+  __TEXT.__unwind_info: 0x5580
   __TEXT.__objc_classname: 0x753
-  __TEXT.__objc_methname: 0xebc6
-  __TEXT.__objc_methtype: 0x8d44
-  __TEXT.__objc_stubs: 0xb8c0
+  __TEXT.__objc_methname: 0xec15
+  __TEXT.__objc_methtype: 0x9b0b
+  __TEXT.__objc_stubs: 0xb900
   __DATA_CONST.__got: 0xd80
-  __DATA_CONST.__const: 0xac50
+  __DATA_CONST.__const: 0xac78
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ce8
+  __DATA_CONST.__objc_selrefs: 0x3cf8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x3338
   __AUTH_CONST.__auth_ptr: 0x258
-  __AUTH_CONST.__const: 0x77068
+  __AUTH_CONST.__const: 0x77088
   __AUTH_CONST.__cfstring: 0x95c0
-  __AUTH_CONST.__objc_const: 0x6c98
+  __AUTH_CONST.__objc_const: 0x6cb8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__data: 0x1ad8
   __AUTH.__thread_vars: 0x90
   __AUTH.__thread_bss: 0x2e0
-  __DATA.__objc_ivar: 0x384
+  __DATA.__objc_ivar: 0x388
   __DATA.__data: 0x247e0
   __DATA.__bss: 0x7950
   __DATA.__common: 0x85f8
   __DATA_DIRTY.__objc_ivar: 0x10c
   __DATA_DIRTY.__data: 0x3a8
-  __DATA_DIRTY.__bss: 0x2f9f8
+  __DATA_DIRTY.__bss: 0x2fa08
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 66118
-  Symbols:   74150
-  CStrings:  20443
+  Functions: 66127
+  Symbols:   74159
+  CStrings:  20460
 
CStrings:
+ "AudioManager media services interrupt notification: Fetching new session complete: %@"
+ "AudioManager media services interrupt notification: Fetching new session..."
+ "AudioManager media services interrupted notification: handler has gone away, doing nothing."
+ "AudioManager media services lost notification: Fetching new session complete: %@"
+ "AudioManager media services lost notification: Fetching new session..."
+ "AudioManager media services lost notification: handler has gone away, doing nothing."
+ "AudioManager media services reset notification: Fetching new session complete: %@"
+ "AudioManager media services reset notification: Fetching new session..."
+ "[RE/MediaServices] Media services recovered, but engine was shutdown. %@"
+ "[RE] [AudioMultiSceneManager] Audio asset: %llu has been unregistered. Not storing assetData in asset generator map."
+ "[RE] [AudioSharedSceneManager] Audio asset: %llu has been unregistered. Not storing assetData in asset generator map."
+ "_callbackRegistry"
+ "forceColorWriteMaskNone"
+ "registerTriggerCallback:callback:"
+ "unregisterTriggerCallback:"
+ "v32@0:8{REAudioServicesNotificationCallbackConfiguration=CCQ}16"
+ "v40@0:8{REAudioServicesNotificationCallbackConfiguration=CCQ}16@?32"
+ "{REAudioServicesNotificationCallbackRegistry=\"m_registry\"{unordered_map<REAudioServicesNotificationCallbackConfiguration, void (^)(), REAudioServicesNotificationCallbackRegistry::ConfigHasher, std::equal_to<REAudioServicesNotificationCallbackConfiguration>, std::allocator<std::pair<const REAudioServicesNotificationCallbackConfiguration, void (^)()>>>=\"__table_\"{__hash_table<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, std::__unordered_map_hasher<REAudioServicesNotificationCallbackConfiguration, std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, REAudioServicesNotificationCallbackRegistry::ConfigHasher, std::equal_to<REAudioServicesNotificationCallbackConfiguration>>, std::__unordered_map_equal<REAudioServicesNotificationCallbackConfiguration, std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, std::equal_to<REAudioServicesNotificationCallbackConfiguration>, REAudioServicesNotificationCallbackRegistry::ConfigHasher>, std::allocator<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<REAudioServicesNotificationCallbackConfiguration, std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, REAudioServicesNotificationCallbackRegistry::ConfigHasher, std::equal_to<REAudioServicesNotificationCallbackConfiguration>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<REAudioServicesNotificationCallbackConfiguration, std::__hash_value_type<REAudioServicesNotificationCallbackConfiguration, void (^)()>, std::equal_to<REAudioServicesNotificationCallbackConfiguration>, REAudioServicesNotificationCallbackRegistry::ConfigHasher>>=\"__value_\"f}}}}"
- "[RE/MediaServices] Media services restored, but engine was shutdown. %@"

```
