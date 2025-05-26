## CommunicationsFilter

> `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter`

```diff

-133.200.1.5.1
-  __TEXT.__text: 0x25c8
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x1f0
+133.300.51.0.0
+  __TEXT.__text: 0x2bb4
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_methlist: 0x270
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x1e2
-  __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__oslogstring: 0x306
-  __TEXT.__unwind_info: 0x160
-  __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methname: 0x56b
-  __TEXT.__objc_methtype: 0x16c
-  __TEXT.__objc_stubs: 0x6e0
+  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__oslogstring: 0x3d7
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_classname: 0x95
+  __TEXT.__objc_methname: 0x6a3
+  __TEXT.__objc_methtype: 0x1b8
+  __TEXT.__objc_stubs: 0x760
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2c8
-  __DATA_CONST.__objc_selrefs: 0x1e0
+  __DATA_CONST.__objc_const: 0x418
+  __DATA_CONST.__objc_selrefs: 0x228
   __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x1a8
-  __DATA.__objc_classrefs: 0x58
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x30
+  __AUTH_CONST.__objc_const: 0x48
+  __AUTH_CONST.__auth_got: 0x230
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_classrefs: 0x60
+  __DATA.__objc_superrefs: 0x28
+  __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x38
   __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__objc_const: 0x168

   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 66
-  Symbols:   317
-  CStrings:  147
+  Functions: 81
+  Symbols:   385
+  CStrings:  177
 
Symbols:
+ -[CMFNotificationObserver .cxx_destruct]
+ -[CMFNotificationObserver callback]
+ -[CMFNotificationObserver dealloc]
+ -[CMFNotificationObserver initWithName:queue:callback:]
+ -[CMFNotificationObserver name]
+ -[CMFNotificationObserver queue]
+ -[CMFNotificationObserver setToken:]
+ -[CMFNotificationObserver token]
+ -[CommunicationFilterItemCache .cxx_destruct]
+ -[CommunicationsFilterBlockList addItemForAllServices:].cold.1
+ -[CommunicationsFilterBlockList removeItemForAllServices:].cold.1
+ -[CommunicationsFilterBlockListCache .cxx_destruct]
+ -[CommunicationsFilterBlockListCache _blockListChanged]
+ -[CommunicationsFilterBlockListCache blockListUpdateObserver]
+ GCC_except_table0
+ GCC_except_table10
+ GCC_except_table12
+ GCC_except_table5
+ _OBJC_CLASS_$_CMFNotificationObserver
+ _OBJC_CLASS_$_NSString
+ _OBJC_IVAR_$_CMFNotificationObserver._callback
+ _OBJC_IVAR_$_CMFNotificationObserver._name
+ _OBJC_IVAR_$_CMFNotificationObserver._queue
+ _OBJC_IVAR_$_CMFNotificationObserver._token
+ _OBJC_IVAR_$_CommunicationsFilterBlockListCache._blockListUpdateObserver
+ _OBJC_METACLASS_$_CMFNotificationObserver
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_INSTANCE_METHODS_CMFNotificationObserver
+ __OBJC_$_INSTANCE_VARIABLES_CMFNotificationObserver
+ __OBJC_$_PROP_LIST_CMFNotificationObserver
+ __OBJC_$_PROP_LIST_CommunicationsFilterBlockListCache
+ __OBJC_CLASS_RO_$_CMFNotificationObserver
+ __OBJC_METACLASS_RO_$_CMFNotificationObserver
+ ___42-[CommunicationsFilterBlockListCache init]_block_invoke_2
+ ___55-[CMFNotificationObserver initWithName:queue:callback:]_block_invoke
+ ___block_descriptor_40_e8_32s_e8_v12?0i8ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ __os_log_fault_impl
+ _notify_cancel
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_blockListChanged
+ _objc_msgSend$callback
+ _objc_msgSend$initWithName:queue:callback:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x23
+ _objc_retainBlock
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_storeStrong
- -[CommunicationFilterItemCache dealloc]
- -[CommunicationsFilterBlockListCache _blockListChanged:]
- GCC_except_table11
- GCC_except_table6
- _OBJC_CLASS_$_NSDistributedNotificationCenter
- ___block_descriptor_40_e8_32o_e8_v12?0i8ls32l8
- _objc_msgSend$addObserver:selector:name:object:
- _objc_retain_x20
CStrings:
+ "\x01"
+ "\x01\x11"
+ "\x13"
+ ".cxx_destruct"
+ "@\"CMFNotificationObserver\""
+ "@40@0:8@16@24@?32"
+ "@?"
+ "@?16@0:8"
+ "CMFNotificationObserver"
+ "Client is requesting to add an invalid item to the block list - will not notify server of any changes"
+ "Client is requesting to remove an invalid item from the block list - will not notify server of any changes"
+ "T@\"CMFNotificationObserver\",R,N,V_blockListUpdateObserver"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSString\",R,C,N,V_name"
+ "T@?,R,C,N,V_callback"
+ "Ti,N,V_token"
+ "UTF8String"
+ "_blockListChanged"
+ "_blockListUpdateObserver"
+ "_callback"
+ "_name"
+ "_token"
+ "blockListUpdateObserver"
+ "callback"
+ "i16@0:8"
+ "initWithName:queue:callback:"
+ "name"
+ "queue"
+ "setToken:"
+ "stringWithUTF8String:"
+ "token"
+ "v20@0:8i16"
- "_blockListChanged:"
- "addObserver:selector:name:object:"

```
