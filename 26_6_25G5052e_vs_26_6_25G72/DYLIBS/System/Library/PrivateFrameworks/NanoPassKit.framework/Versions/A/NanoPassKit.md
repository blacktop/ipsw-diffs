## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/Versions/A/NanoPassKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`

```diff

-1289.19.0.0.0
-  __TEXT.__text: 0x11983c
+1289.26.0.0.0
+  __TEXT.__text: 0x11a2ec
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x18864
+  __TEXT.__objc_methlist: 0x188fc
   __TEXT.__cstring: 0x85f9
   __TEXT.__const: 0x21a
   __TEXT.__gcc_except_tab: 0xcd0
-  __TEXT.__oslogstring: 0x428b
+  __TEXT.__oslogstring: 0x4517
   __TEXT.__ustring: 0x160
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x9
   __TEXT.__swift5_reflstr: 0x17
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x5f58
-  __TEXT.__objc_classname: 0x4d68
-  __TEXT.__objc_methname: 0x17e9a
-  __TEXT.__objc_methtype: 0x2363
-  __TEXT.__objc_stubs: 0xafc0
-  __DATA_CONST.__got: 0x680
+  __TEXT.__unwind_info: 0x5f70
+  __TEXT.__objc_classname: 0x4dcb
+  __TEXT.__objc_methname: 0x17fde
+  __TEXT.__objc_methtype: 0x239e
+  __TEXT.__objc_stubs: 0xb080
+  __DATA_CONST.__got: 0x6b0
   __DATA_CONST.__const: 0x740
-  __DATA_CONST.__objc_classlist: 0xd98
+  __DATA_CONST.__objc_classlist: 0xda8
   __DATA_CONST.__objc_catlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5840
+  __DATA_CONST.__objc_selrefs: 0x5888
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xd78
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0x1110
   __AUTH_CONST.__cfstring: 0x72a0
-  __AUTH_CONST.__objc_const: 0x28890
+  __AUTH_CONST.__objc_const: 0x28d18
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x87f0
+  __AUTH.__objc_data: 0x8890
   __DATA.__objc_ivar: 0x11b0
-  __DATA.__data: 0x488
+  __DATA.__data: 0x4e8
   __DATA.__bss: 0xe8
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8776
-  Symbols:   15452
-  CStrings:  5702
+  Functions: 8783
+  Symbols:   15488
+  CStrings:  5727
 
Symbols:
+ +[NPKPassLibraryNotificationBroadcaster firePassAddedNotificationWithUniqueID:passSource:]
+ +[NPKPassLibraryNotificationBroadcaster firePassRemovedNotificationWithUniqueID:]
+ +[NPKPassLibraryNotificationBroadcaster firePassUpdatedNotificationWithUniqueID:passSource:]
+ -[NPKPassLibraryCoordinator _createConnection]
+ -[NPKPassLibraryCoordinator notePassAddedWithUniqueID:passSource:]
+ -[NPKPassLibraryCoordinator notePassRemovedWithUniqueID:]
+ -[NPKPassLibraryCoordinator notePassUpdatedWithUniqueID:passSource:]
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
+ _objc_msgSend$_createConnection
+ _objc_msgSend$notePassAddedWithUniqueID:passSource:
+ _objc_msgSend$notePassRemovedWithUniqueID:
+ _objc_msgSend$notePassUpdatedWithUniqueID:passSource:
+ _objc_msgSend$notificationWithName:object:userInfo:
+ _objc_msgSend$postNotification:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Kc3mvo/Sources/NanoPassbook_Frameworks/NanoPassKit/NPKOSTransaction.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Kc3mvo/Sources/NanoPassbook_Frameworks/NanoPassKit/NPKSubcredentialProvisioningService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Kc3mvo/Sources/NanoPassbook_Frameworks/NanoPassKit/NPKWorkQueue.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Kc3mvo/Sources/NanoPassbook_Frameworks/NanoPassKit/PKPass+NanoPassKit.m"
+ "Error: Failed to create connection for pass library notification"
+ "NPKPassLibraryCoordinator"
+ "NPKPassLibraryNotificationBroadcaster"
+ "NPKPassLibraryNotificationProtocol"
+ "Notice: Attempting to notify process of added pass with passUniqueID: %@"
+ "Notice: Attempting to notify process of removed pass with passUniqueID: %@"
+ "Notice: Attempting to notify process of updated pass with passUniqueID: %@"
+ "Notice: Cannot notify process of added pass with nil passUniqueID"
+ "Notice: Cannot notify process of removed pass with nil passUniqueID"
+ "Notice: Cannot notify process of updated pass with nil passUniqueID"
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
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8@\"NSString\"16q24"
+ "v32@0:8@16q24"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MPhy5o/Sources/NanoPassbook_Frameworks/NanoPassKit/NPKOSTransaction.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MPhy5o/Sources/NanoPassbook_Frameworks/NanoPassKit/NPKSubcredentialProvisioningService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MPhy5o/Sources/NanoPassbook_Frameworks/NanoPassKit/NPKWorkQueue.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MPhy5o/Sources/NanoPassbook_Frameworks/NanoPassKit/PKPass+NanoPassKit.m"
```
