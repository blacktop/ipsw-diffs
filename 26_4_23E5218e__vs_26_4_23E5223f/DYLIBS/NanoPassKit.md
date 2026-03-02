## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1289.18.1.0.0
-  __TEXT.__text: 0x1f01a0
+1289.20.0.0.0
+  __TEXT.__text: 0x1f12ec
   __TEXT.__auth_stubs: 0x13d0
-  __TEXT.__objc_methlist: 0x1ec10
+  __TEXT.__objc_methlist: 0x1ecd0
   __TEXT.__cstring: 0x12496
   __TEXT.__const: 0x2aa
   __TEXT.__gcc_except_tab: 0x4f50
-  __TEXT.__oslogstring: 0x20cf4
+  __TEXT.__oslogstring: 0x2118b
   __TEXT.__dlopen_cstrs: 0x1ba
   __TEXT.__ustring: 0x160
   __TEXT.__constg_swiftt: 0x28

   __TEXT.__swift5_reflstr: 0x17
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8718
-  __TEXT.__objc_classname: 0x573f
-  __TEXT.__objc_methname: 0x2a276
-  __TEXT.__objc_methtype: 0x6e8a
-  __TEXT.__objc_stubs: 0x157a0
-  __DATA_CONST.__got: 0x1540
+  __TEXT.__unwind_info: 0x8738
+  __TEXT.__objc_classname: 0x57a2
+  __TEXT.__objc_methname: 0x2a3ba
+  __TEXT.__objc_methtype: 0x6ea2
+  __TEXT.__objc_stubs: 0x15860
+  __DATA_CONST.__got: 0x1570
   __DATA_CONST.__const: 0x4078
-  __DATA_CONST.__objc_classlist: 0xed8
+  __DATA_CONST.__objc_classlist: 0xee8
   __DATA_CONST.__objc_catlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x160
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b60
+  __DATA_CONST.__objc_selrefs: 0x8ba8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0xe90
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x9f8
   __AUTH_CONST.__const: 0x740
   __AUTH_CONST.__cfstring: 0xa660
-  __AUTH_CONST.__objc_const: 0x34b80
+  __AUTH_CONST.__objc_const: 0x35118
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x9380
+  __AUTH.__objc_data: 0x9420
   __DATA.__objc_ivar: 0x15d8
-  __DATA.__data: 0x10c0
+  __DATA.__data: 0x1120
   __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C39CC4A9-4FA4-3730-8C61-CBE9A8BC8947
-  Functions: 11483
-  Symbols:   33138
-  CStrings:  12160
+  UUID: 488B3F0F-C1E9-39FB-B771-37A5F5DF5C91
+  Functions: 11496
+  Symbols:   33203
+  CStrings:  12189
 
Symbols:
+ +[NPKPassLibraryNotificationBroadcaster firePassAddedNotificationWithUniqueID:passSource:]
+ +[NPKPassLibraryNotificationBroadcaster firePassRemovedNotificationWithUniqueID:]
+ +[NPKPassLibraryNotificationBroadcaster firePassUpdatedNotificationWithUniqueID:passSource:]
+ -[NPKCompanionAgentConnection notePassAddedWithUniqueID:passSource:]
+ -[NPKCompanionAgentConnection notePassRemovedWithUniqueID:]
+ -[NPKCompanionAgentConnection notePassUpdatedWithUniqueID:passSource:]
+ -[NPKPassLibraryCoordinator _createConnection]
+ -[NPKPassLibraryCoordinator notePassAddedWithUniqueID:passSource:]
+ -[NPKPassLibraryCoordinator notePassRemovedWithUniqueID:]
+ -[NPKPassLibraryCoordinator notePassUpdatedWithUniqueID:passSource:]
+ GCC_except_table250
+ GCC_except_table278
+ _OBJC_CLASS_$_NPKPassLibraryCoordinator
+ _OBJC_CLASS_$_NPKPassLibraryNotificationBroadcaster
+ _OBJC_CLASS_$_NSNotification
+ _OBJC_METACLASS_$_NPKPassLibraryCoordinator
+ _OBJC_METACLASS_$_NPKPassLibraryNotificationBroadcaster
+ _PKPassLibraryDidAddPassNotification
+ _PKPassLibraryDidRemovePassNotification
+ _PKPassLibraryDidUpdatePassNotification
+ _PKPassLibraryPassSourceUserInfoKey
+ _PKPassLibraryUniqueIDUserInfoKey
+ __OBJC_$_CLASS_METHODS_NPKPassLibraryNotificationBroadcaster
+ __OBJC_$_INSTANCE_METHODS_NPKPassLibraryCoordinator
+ __OBJC_$_PROP_LIST_NPKPassLibraryCoordinator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NPKPassLibraryNotificationProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NPKPassLibraryNotificationProtocol
+ __OBJC_$_PROTOCOL_REFS_NPKPassLibraryNotificationProtocol
+ __OBJC_CLASS_PROTOCOLS_$_NPKPassLibraryCoordinator
+ __OBJC_CLASS_RO_$_NPKPassLibraryCoordinator
+ __OBJC_CLASS_RO_$_NPKPassLibraryNotificationBroadcaster
+ __OBJC_LABEL_PROTOCOL_$_NPKPassLibraryNotificationProtocol
+ __OBJC_METACLASS_RO_$_NPKPassLibraryCoordinator
+ __OBJC_METACLASS_RO_$_NPKPassLibraryNotificationBroadcaster
+ __OBJC_PROTOCOL_$_NPKPassLibraryNotificationProtocol
+ ___59-[NPKCompanionAgentConnection notePassRemovedWithUniqueID:]_block_invoke
+ ___68-[NPKCompanionAgentConnection notePassAddedWithUniqueID:passSource:]_block_invoke
+ ___70-[NPKCompanionAgentConnection notePassUpdatedWithUniqueID:passSource:]_block_invoke
+ _objc_msgSend$_createConnection
+ _objc_msgSend$notePassAddedWithUniqueID:passSource:
+ _objc_msgSend$notePassRemovedWithUniqueID:
+ _objc_msgSend$notePassUpdatedWithUniqueID:passSource:
+ _objc_msgSend$notificationWithName:object:userInfo:
+ _objc_msgSend$postNotification:
- GCC_except_table244
- GCC_except_table272
CStrings:
+ "Error: Failed to create connection for pass library notification"
+ "Error: NPKCompanionAgentConnection (%@): Failed to note pass added with unique ID: %@"
+ "Error: NPKCompanionAgentConnection (%@): Failed to note pass removed with unique ID: %@"
+ "Error: NPKCompanionAgentConnection (%@): Failed to note pass updated with unique ID: %@"
+ "NPKPassLibraryCoordinator"
+ "NPKPassLibraryNotificationBroadcaster"
+ "NPKPassLibraryNotificationProtocol"
+ "Notice: Attempting to notify process of added pass with passUniqueID: %@"
+ "Notice: Attempting to notify process of removed pass with passUniqueID: %@"
+ "Notice: Attempting to notify process of updated pass with passUniqueID: %@"
+ "Notice: Cannot notify process of added pass with nil passUniqueID"
+ "Notice: Cannot notify process of removed pass with nil passUniqueID"
+ "Notice: Cannot notify process of updated pass with nil passUniqueID"
+ "Notice: NPKCompanionAgentConnection (%@): Note pass added with unique ID: %@, source: %lu"
+ "Notice: NPKCompanionAgentConnection (%@): Note pass removed with unique ID: %@"
+ "Notice: NPKCompanionAgentConnection (%@): Note pass updated with unique ID: %@, source: %lu"
+ "Notice: Note pass added with unique ID %@ from source %lu"
+ "Notice: Note pass removed with unique ID %@"
+ "Notice: Note pass updated with unique ID %@ from source %lu"
+ "_createConnection"
+ "firePassAddedNotificationWithUniqueID:passSource:"
+ "firePassRemovedNotificationWithUniqueID:"
+ "firePassUpdatedNotificationWithUniqueID:passSource:"
+ "notePassAddedWithUniqueID:passSource:"
+ "notePassRemovedWithUniqueID:"
+ "notePassUpdatedWithUniqueID:passSource:"
+ "notificationWithName:object:userInfo:"
+ "postNotification:"
+ "v32@0:8@\"NSString\"16q24"

```
