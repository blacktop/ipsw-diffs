## SoundScapesUtility

> `/System/Library/PrivateFrameworks/SoundScapesUtility.framework/SoundScapesUtility`

```diff

-202.50.1.0.0
-  __TEXT.__text: 0x19bc
-  __TEXT.__auth_stubs: 0x2a0
+264.0.0.0.0
+  __TEXT.__text: 0x17e8
   __TEXT.__objc_methlist: 0x320
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0xf4
-  __TEXT.__gcc_except_tab: 0x50
+  __TEXT.__cstring: 0xfc
+  __TEXT.__gcc_except_tab: 0x24
   __TEXT.__oslogstring: 0xe9
-  __TEXT.__unwind_info: 0x110
-  __TEXT.__objc_classname: 0xbf
-  __TEXT.__objc_methname: 0xa1a
-  __TEXT.__objc_methtype: 0x30e
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0x80
+  __TEXT.__unwind_info: 0x108
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x5c0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x180

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9F3EDB0-6FCD-3C29-80CF-FB809FC98361
+  UUID: 626E5A47-CB6E-35DB-A087-5214B6171ABB
   Functions: 46
-  Symbols:   313
-  CStrings:  202
+  Symbols:   315
+  CStrings:  24
 
Symbols:
+ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke.140
+ ___block_literal_global.117
+ ___block_literal_global.133
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x4
+ _objc_retain_x8
- ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke.141
- ___block_literal_global.118
- ___block_literal_global.134
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x27
Functions:
~ __SSULoggingFacility : 84 -> 68
~ -[SSUSoundScapesMediaProfile initWithAccessory:forHome:] : 136 -> 140
~ -[_SSUSoundScapesDelegateForwarder initForViewController:] : 568 -> 516
~ ___61-[_SSUSoundScapesDelegateForwarder mediaPickerConfirmChoices]_block_invoke : 88 -> 84
~ -[_SSUSoundScapesDelegateForwarder selectedSoundScapes:withError:] : 192 -> 204
~ ___50-[_SSUSoundScapesDelegateForwarder requestDismiss]_block_invoke : 80 -> 76
~ -[_SSUSoundScapesDelegateForwarder pickerDismissed] : 200 -> 184
~ ___43-[_SSUSoundScapesDelegateForwarder cleanup]_block_invoke : 72 -> 68
~ +[SSUSoundScapesPickerManager sharedManager] : 176 -> 160
~ -[SSUSoundScapesPickerManager init] : 152 -> 144
~ -[SSUSoundScapesPickerManager registerViewController:forMediaProfiles:andDelegate:] : 172 -> 176
~ +[SSUSoundScapesPickerManager pickerSupportHome:targetMediaProfiles:] : 88 -> 80
~ +[SSUSoundScapesPickerManager pickerIdentity] : 84 -> 68
~ ___45+[SSUSoundScapesPickerManager pickerIdentity]_block_invoke : 200 -> 188
~ +[SSUSoundScapesPickerManager pickerForMediaProfiles:forDelegate:] : 1216 -> 1072
~ -[SSUSoundScapesPickerManager hostViewControllerDidActivate:] : 1056 -> 952
~ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke : 116 -> 104
~ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke_2 : 256 -> 244
~ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke_3 : 108 -> 100
~ ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke.141 -> ___61-[SSUSoundScapesPickerManager hostViewControllerDidActivate:]_block_invoke.140 : 124 -> 120
~ -[SSUSoundScapesPickerManager hostViewControllerWillDeactivate:error:] : 136 -> 132
~ -[SSUSoundScapesPickerManager hostViewControllerDidActivate:].cold.1 : 120 -> 76
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SSUSoundscapesPickerControllerDelegate>\""
- "@\"HMAccessory\""
- "@\"HMHome\""
- "@\"MPPlaybackArchive\""
- "@\"NSError\""
- "@\"NSMapTable\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"UIBarButtonItem\""
- "@\"_EXHostViewController\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSXPCConnection\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "NSObject"
- "Q16@0:8"
- "SSURemoteViewServiceProtocol"
- "SSUSoundScapesMediaProfile"
- "SSUSoundScapesPickerManager"
- "SSUViewServiceHostProtocol"
- "T#,R"
- "T@\"<SSUSoundscapesPickerControllerDelegate>\",W,V_delegate"
- "T@\"HMAccessory\",W,V_backingAccessory"
- "T@\"HMHome\",W,V_home"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,V_connection"
- "T@\"_EXHostViewController\",W,V_viewController"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_EXHostViewControllerDelegate"
- "_SSUSoundScapesDelegateForwarder"
- "_backingAccessory"
- "_connection"
- "_delegate"
- "_delegates"
- "_doneButton"
- "_exiting"
- "_home"
- "_lastPickedArchive"
- "_lastPickedError"
- "_targetMediaProfile"
- "_viewController"
- "accessories"
- "addSubview:"
- "allObjects"
- "anyObject"
- "autorelease"
- "backingAccessory"
- "bundleWithURL:"
- "capabilities"
- "centerXAnchor"
- "centerYAnchor"
- "class"
- "cleanup"
- "conformsToProtocol:"
- "connection"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "debugDescription"
- "delegate"
- "description"
- "device"
- "executeQuery:"
- "firstObject"
- "hash"
- "home"
- "hostViewController:didBeginHosting:"
- "hostViewController:didEndHosting:error:"
- "hostViewController:didFailToHost:error:"
- "hostViewController:didPrepareToHost:"
- "hostViewControllerDidActivate:"
- "hostViewControllerWillDeactivate:error:"
- "init"
- "initForViewController:"
- "initWithAccessory:forHome:"
- "initWithConfiguration:"
- "initWithExtensionIdentity:"
- "initWithExtensionPointIdentifier:"
- "initWithTitle:style:target:action:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "leadingAnchor"
- "localizedStringForKey:value:table:"
- "makeXPCConnectionWithError:"
- "mapTableWithKeyOptions:valueOptions:"
- "mediaPickerCancelled"
- "mediaPickerConfirmChoices"
- "mediaPickerDidSelectPlaybackArchive:withError:"
- "na_firstObjectPassingTest:"
- "na_map:"
- "navigationItem"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pickerDismissed"
- "pickerForMediaProfiles:forDelegate:"
- "pickerIdentity"
- "pickerSupportHome:targetMediaProfiles:"
- "placeholderView"
- "registerViewController:forMediaProfiles:andDelegate:"
- "release"
- "remoteObjectProxy"
- "removeObjectForKey:"
- "requestDismiss"
- "residentDevices"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "safeAreaLayoutGuide"
- "selectedSoundScapes:withError:"
- "self"
- "setActive:"
- "setBackgroundColor:"
- "setBackingAccessory:"
- "setClipsToBounds:"
- "setConnection:"
- "setDelegate:"
- "setEnabled:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHidden:"
- "setHome:"
- "setInvalidationHandler:"
- "setLargeTitleDisplayMode:"
- "setObject:forKey:"
- "setPlaceholderView:"
- "setRemoteObjectInterface:"
- "setRightBarButtonItem:"
- "setTag:"
- "setText:"
- "setTextAlignment:"
- "setTitle:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setViewController:"
- "setupDataSourceWithTargetDeviceVersions:andFallbackResidentDeviceVersions:"
- "sharedManager"
- "shortVersionString"
- "shouldAcceptXPCConnection:"
- "softwareVersion"
- "superclass"
- "systemBackgroundColor"
- "topAnchor"
- "updateNavigationItem"
- "url"
- "v16@0:8"
- "v24@0:8@\"_EXHostViewController\"16"
- "v24@0:8@16"
- "v32@0:8@\"MPPlaybackArchive\"16@\"NSError\"24"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"_EXHostViewController\"16@\"NSError\"24"
- "v32@0:8@\"_EXHostViewController\"16@\"_EXHostViewControllerConfiguration\"24"
- "v32@0:8@16@24"
- "v40@0:8@\"_EXHostViewController\"16@\"_EXHostViewControllerConfiguration\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "view"
- "viewController"
- "viewWithTag:"
- "zone"

```
