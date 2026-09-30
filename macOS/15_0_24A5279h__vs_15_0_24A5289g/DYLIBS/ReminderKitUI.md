## ReminderKitUI

> `/System/Library/PrivateFrameworks/ReminderKitUI.framework/Versions/A/ReminderKitUI`

```diff

-1093.0.0.0.0
-  __TEXT.__text: 0x2c7c
+1095.0.0.0.0
+  __TEXT.__text: 0x1e44
   __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_methlist: 0x594
+  __TEXT.__objc_methlist: 0x3d4
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1f0
+  __TEXT.__cstring: 0x1af
   __TEXT.__oslogstring: 0x174
-  __TEXT.__unwind_info: 0x150
-  __TEXT.__objc_classname: 0x19a
-  __TEXT.__objc_methname: 0x1324
-  __TEXT.__objc_methtype: 0x44f
-  __TEXT.__objc_stubs: 0xce0
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_classname: 0x138
+  __TEXT.__objc_methname: 0xec6
+  __TEXT.__objc_methtype: 0x35c
+  __TEXT.__objc_stubs: 0xa60
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x410
+  __DATA_CONST.__objc_selrefs: 0x328
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0x90
-  __AUTH_CONST.__cfstring: 0x240
-  __AUTH_CONST.__objc_const: 0xeb0
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x64
+  __AUTH_CONST.__cfstring: 0x1c0
+  __AUTH_CONST.__objc_const: 0xb00
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x48
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 118
-  Symbols:   403
-  CStrings:  22
+  Functions: 85
+  Symbols:   310
+  CStrings:  18
 
Symbols:
+ -[REMReminderCreationRemoteViewController viewServiceDidFinish]
+ -[REMReminderCreationViewController sendDidCreate:error:]
+ -[REMReminderCreationViewController viewServiceDidFinish]
+ -[REMReminderServiceViewController viewServiceDidFinish]
+ _objc_msgSend$sendDidCreate:error:
+ _objc_msgSend$viewServiceDidFinish
- +[REMReminderEditingContext supportsSecureCoding]
- +[REMReminderServiceOptimisticResult supportsSecureCoding]
- -[REMReminderCreationRemoteViewController viewServiceDidFinishWithResult:]
- -[REMReminderCreationViewController sendDidCreateWithResult:error:]
- -[REMReminderCreationViewController viewServiceDidFinishWithResult:]
- -[REMReminderEditingContext .cxx_destruct]
- -[REMReminderEditingContext encodeWithCoder:]
- -[REMReminderEditingContext initWithCoder:]
- -[REMReminderEditingContext initWithReminderID:]
- -[REMReminderEditingContext reminderID]
- -[REMReminderEditingContext setReminderID:]
- -[REMReminderEditingViewController .cxx_destruct]
- -[REMReminderEditingViewController delegate]
- -[REMReminderEditingViewController editingContext]
- -[REMReminderEditingViewController initWithEditingContext:]
- -[REMReminderEditingViewController remoteViewControllerDidLoad:setupCompletion:]
- -[REMReminderEditingViewController sendDidEditWithResult:error:]
- -[REMReminderEditingViewController setDelegate:]
- -[REMReminderEditingViewController setEditingContext:]
- -[REMReminderEditingViewController viewServiceDidCancel]
- -[REMReminderEditingViewController viewServiceDidFailWithError:]
- -[REMReminderEditingViewController viewServiceDidFinishWithResult:]
- -[REMReminderServiceOptimisticResult .cxx_destruct]
- -[REMReminderServiceOptimisticResult accountStorage]
- -[REMReminderServiceOptimisticResult encodeWithCoder:]
- -[REMReminderServiceOptimisticResult initWithCoder:]
- -[REMReminderServiceOptimisticResult initWithReminder:]
- -[REMReminderServiceOptimisticResult initWithReminderStorage:parentReminderStorage:listStorage:accountStorage:]
- -[REMReminderServiceOptimisticResult listStorage]
- -[REMReminderServiceOptimisticResult parentReminderStorage]
- -[REMReminderServiceOptimisticResult reminderStorage]
- -[REMReminderServiceOptimisticResult reminderWithStore:]
- -[REMReminderServiceOptimisticResult setAccountStorage:]
- -[REMReminderServiceOptimisticResult setListStorage:]
- -[REMReminderServiceOptimisticResult setParentReminderStorage:]
- -[REMReminderServiceOptimisticResult setReminderStorage:]
- -[REMReminderServiceViewController viewServiceDidFinishWithResult:]
- OBJC_IVAR_$_REMReminderEditingContext._reminderID
- OBJC_IVAR_$_REMReminderEditingViewController._delegate
- OBJC_IVAR_$_REMReminderEditingViewController._editingContext
- OBJC_IVAR_$_REMReminderServiceOptimisticResult._accountStorage
- OBJC_IVAR_$_REMReminderServiceOptimisticResult._listStorage
- OBJC_IVAR_$_REMReminderServiceOptimisticResult._parentReminderStorage
- OBJC_IVAR_$_REMReminderServiceOptimisticResult._reminderStorage
- _OBJC_CLASS_$_REMAccount
- _OBJC_CLASS_$_REMAccountStorage
- _OBJC_CLASS_$_REMList
- _OBJC_CLASS_$_REMListStorage
- _OBJC_CLASS_$_REMReminder
- _OBJC_CLASS_$_REMReminderEditingContext
- _OBJC_CLASS_$_REMReminderEditingViewController
- _OBJC_CLASS_$_REMReminderServiceOptimisticResult
- _OBJC_CLASS_$_REMReminderStorage
- _OBJC_METACLASS_$_REMReminderEditingContext
- _OBJC_METACLASS_$_REMReminderEditingViewController
- _OBJC_METACLASS_$_REMReminderServiceOptimisticResult
- __OBJC_$_CLASS_METHODS_REMReminderEditingContext
- __OBJC_$_CLASS_METHODS_REMReminderServiceOptimisticResult
- __OBJC_$_CLASS_PROP_LIST_REMReminderEditingContext
- __OBJC_$_CLASS_PROP_LIST_REMReminderServiceOptimisticResult
- __OBJC_$_INSTANCE_METHODS_REMReminderEditingContext
- __OBJC_$_INSTANCE_METHODS_REMReminderEditingViewController
- __OBJC_$_INSTANCE_METHODS_REMReminderServiceOptimisticResult
- __OBJC_$_INSTANCE_VARIABLES_REMReminderEditingContext
- __OBJC_$_INSTANCE_VARIABLES_REMReminderEditingViewController
- __OBJC_$_INSTANCE_VARIABLES_REMReminderServiceOptimisticResult
- __OBJC_$_PROP_LIST_REMReminderEditingContext
- __OBJC_$_PROP_LIST_REMReminderEditingViewController
- __OBJC_$_PROP_LIST_REMReminderServiceOptimisticResult
- __OBJC_CLASS_PROTOCOLS_$_REMReminderEditingContext
- __OBJC_CLASS_PROTOCOLS_$_REMReminderServiceOptimisticResult
- __OBJC_CLASS_RO_$_REMReminderEditingContext
- __OBJC_CLASS_RO_$_REMReminderEditingViewController
- __OBJC_CLASS_RO_$_REMReminderServiceOptimisticResult
- __OBJC_METACLASS_RO_$_REMReminderEditingContext
- __OBJC_METACLASS_RO_$_REMReminderEditingViewController
- __OBJC_METACLASS_RO_$_REMReminderServiceOptimisticResult
- _objc_msgSend$account
- _objc_msgSend$accountStorage
- _objc_msgSend$displayForEditingWithContext:completion:
- _objc_msgSend$editingContext
- _objc_msgSend$initWithReminderID:
- _objc_msgSend$initWithReminderStorage:parentReminderStorage:listStorage:accountStorage:
- _objc_msgSend$initWithStore:account:storage:
- _objc_msgSend$initWithStore:list:storage:
- _objc_msgSend$initWithStore:storage:
- _objc_msgSend$list
- _objc_msgSend$listStorage
- _objc_msgSend$parentReminder
- _objc_msgSend$parentReminderStorage
- _objc_msgSend$reminderCreationViewController:didCreateReminderWithResult:error:
- _objc_msgSend$reminderEditingViewController:didEditReminder:error:
- _objc_msgSend$reminderEditingViewController:didEditReminderWithResult:error:
- _objc_msgSend$reminderStorage
- _objc_msgSend$sendDidCreateWithResult:error:
- _objc_msgSend$sendDidEditWithResult:error:
- _objc_msgSend$setParentReminder:
- _objc_msgSend$storage
- _objc_msgSend$viewServiceDidFinishWithResult:
CStrings:
- "accountStorage"
- "listStorage"
- "parentReminderStorage"
- "reminderStorage"

```
