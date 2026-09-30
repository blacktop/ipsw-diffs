## AirPlayMirroringModule

> `/System/Library/ControlCenter/Bundles/AirPlayMirroringModule.bundle/AirPlayMirroringModule`

```diff

-4024.610.2.0.0
-  __TEXT.__text: 0x1530
-  __TEXT.__auth_stubs: 0x1d0
+4025.110.87.2.0
+  __TEXT.__text: 0x1bf0
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_methlist: 0x3b4
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__cstring: 0x83
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0xe8
+  __TEXT.__cstring: 0xa2
+  __TEXT.__oslogstring: 0x471
+  __TEXT.__unwind_info: 0x108
   __TEXT.__objc_classname: 0x91
-  __TEXT.__objc_methname: 0xc75
+  __TEXT.__objc_methname: 0xd06
   __TEXT.__objc_methtype: 0x3c5
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0x80
+  __TEXT.__objc_stubs: 0xa60
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c8
+  __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0x138
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0xc0
+  __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x8b8
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MediaControls.framework/MediaControls
+  - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F8D1E88-4EC6-3E01-87E8-076178482916
+  UUID: 024969E9-C07E-3CFE-B750-260FA7796F88
   Functions: 47
-  Symbols:   64
-  CStrings:  200
+  Symbols:   73
+  CStrings:  233
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
+ __MRLogCategoryMirroringView
+ __os_signpost_emit_with_name_impl
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _os_signpost_enabled
Functions:
~ sub_23f071ec8 -> sub_2476aff78 : 364 -> 592
~ sub_23f072034 -> sub_2476b01c8 : 108 -> 256
~ sub_23f0720a0 -> sub_2476b02c8 : 120 -> 304
~ sub_23f072438 -> sub_2476b0718 : 1200 -> 1488
~ sub_23f072a0c -> sub_2476b0e0c : 304 -> 556
~ sub_23f072c14 -> sub_2476b1110 : 324 -> 788
~ sub_23f072f78 -> sub_2476b1644 : 112 -> 276
CStrings:
+ "\"DismissedMirroringModuleUponStopMirroring\""
+ "\"MirrorModuleViewDidLoad\""
+ "\"MirrorModuleViewWillAppear\""
+ "\"MirrorModuleViewWillDisappear\""
+ "\"RemovedMirrorModuleFooterButton\""
+ "\"SetMirrorModuleFooterButton\""
+ "\"UpdatedMirrorMenuItems\""
+ "\"UpdatedMirroringModuleState\""
+ "EVENT: DismissedMirroringModuleUponStopMirroring || EVENT DETAILS: {destinationChangeResult=%{public}@}"
+ "EVENT: MirrorModuleViewDidLoad || EVENT DETAILS: {displayMonitor:{mainConfiguration:{deviceName:%{private}@, hardwareID:%{public}@}, connectedIdentities:%@}"
+ "EVENT: MirrorModuleViewWillAppear || EVENT DETAILS: {isShowMoreExpanded:%{BOOL}u}"
+ "EVENT: MirrorModuleViewWillDisappear || EVENT DETAILS: {glyphState:%{public}@}"
+ "EVENT: RemovedMirrorModuleFooterButton || EVENT DETAILS: {hasFooterButton:%{BOOL}u}"
+ "EVENT: SetMirrorModuleFooterButton || EVENT DETAILS: {hasFooterButton:%{BOOL}u}"
+ "EVENT: UpdatedMirrorMenuItems || EVENT DETAILS: {menuItems{count:%{public}@, items:{symbolName:%{public}@, title:%{private}@, isBusy:%{public}@, isSelected:%{public}@}}}"
+ "EVENT: UpdatedMirroringModuleState || EVENT DETAILS: {isModuleExpanded:%{BOOL}u, isModuleSelected:%{BOOL}u, glyphState:%{public}@}"
+ "busy"
+ "deviceName"
+ "glyphState"
+ "hardwareIdentifier"
+ "hasFooterButton"
+ "isSelected"
+ "mainConfiguration"
+ "numberWithInteger:"
+ "numberWithUnsignedInteger:"
+ "selected"
+ "title"
+ "valueForKey:"

```
