## AirPlayMirroringModule

> `/System/Library/ControlCenter/Bundles/AirPlayMirroringModule.bundle/AirPlayMirroringModule`

```diff

-4025.110.87.2.0
-  __TEXT.__text: 0x1bf0
-  __TEXT.__auth_stubs: 0x250
+4025.110.97.1.0
+  __TEXT.__text: 0x1d70
+  __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_methlist: 0x3b4
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__cstring: 0xa2
-  __TEXT.__oslogstring: 0x471
-  __TEXT.__unwind_info: 0x108
+  __TEXT.__gcc_except_tab: 0xfc
+  __TEXT.__cstring: 0xad
+  __TEXT.__oslogstring: 0x378
+  __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0x91
   __TEXT.__objc_methname: 0xd06
   __TEXT.__objc_methtype: 0x3c5

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x138
+  __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x140
+  __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x8b8
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 024969E9-C07E-3CFE-B750-260FA7796F88
+  UUID: 0A66BE2C-87EC-3B09-A951-6B571DE6461C
   Functions: 47
-  Symbols:   73
-  CStrings:  233
+  Symbols:   74
+  CStrings:  236
 
Symbols:
+ _os_signpost_id_generate
Functions:
~ sub_2476aff78 -> sub_247d1bf78 : 592 -> 624
~ sub_2476b01c8 -> sub_247d1c1e8 : 256 -> 296
~ sub_2476b02c8 -> sub_247d1c310 : 304 -> 336
~ sub_2476b0718 -> sub_247d1c780 : 1488 -> 1556
~ sub_2476b0e0c -> sub_247d1ceb8 : 556 -> 624
~ sub_2476b1110 -> sub_247d1d200 : 788 -> 900
~ sub_2476b1644 -> sub_247d1d7a4 : 276 -> 308
CStrings:
+ "\"UpdatedMirroringModuleStateIsExpanded\""
+ "\"UpdatedMirroringModuleStateModePreview\""
+ "EVENT DETAILS || destinationChangeResult:%{public}@"
+ "EVENT DETAILS || displayMonitor (mainConfiguration) - deviceName:%{private}@, hardwareID:%{public}@}, connectedIdentities:%@"
+ "EVENT DETAILS || glyphState:%{public}@"
+ "EVENT DETAILS || hasFooterButton:%{BOOL}u"
+ "EVENT DETAILS || isModuleExpanded:%{BOOL}u, isModuleSelected:%{BOOL}u, glyphState:%{public}@"
+ "EVENT DETAILS || isShowMoreExpanded:%{BOOL}u"
+ "EVENT DETAILS || menuItems - count:%{public}@, items - symbolName:%{public}@, title:%{private}@, identifier:%{public}@, isBusy:%{public}@, isSelected:%{public}@"
+ "identifier"
- "EVENT: DismissedMirroringModuleUponStopMirroring || EVENT DETAILS: {destinationChangeResult=%{public}@}"
- "EVENT: MirrorModuleViewDidLoad || EVENT DETAILS: {displayMonitor:{mainConfiguration:{deviceName:%{private}@, hardwareID:%{public}@}, connectedIdentities:%@}"
- "EVENT: MirrorModuleViewWillAppear || EVENT DETAILS: {isShowMoreExpanded:%{BOOL}u}"
- "EVENT: MirrorModuleViewWillDisappear || EVENT DETAILS: {glyphState:%{public}@}"
- "EVENT: RemovedMirrorModuleFooterButton || EVENT DETAILS: {hasFooterButton:%{BOOL}u}"
- "EVENT: SetMirrorModuleFooterButton || EVENT DETAILS: {hasFooterButton:%{BOOL}u}"
- "EVENT: UpdatedMirrorMenuItems || EVENT DETAILS: {menuItems{count:%{public}@, items:{symbolName:%{public}@, title:%{private}@, isBusy:%{public}@, isSelected:%{public}@}}}"
- "EVENT: UpdatedMirroringModuleState || EVENT DETAILS: {isModuleExpanded:%{BOOL}u, isModuleSelected:%{BOOL}u, glyphState:%{public}@}"

```
