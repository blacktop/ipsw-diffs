## gamed

> `/usr/libexec/gamed`

```diff

-819.0.71.0.0
-  __TEXT.__text: 0x239a3c
-  __TEXT.__auth_stubs: 0x2e60
-  __TEXT.__objc_stubs: 0x1b500
-  __TEXT.__objc_methlist: 0xc46c
-  __TEXT.__const: 0x12310
+819.0.73.2.2
+  __TEXT.__text: 0x23a450
+  __TEXT.__auth_stubs: 0x2e90
+  __TEXT.__objc_stubs: 0x1b540
+  __TEXT.__objc_methlist: 0xc4bc
+  __TEXT.__const: 0x121e0
   __TEXT.__objc_classname: 0x1eae
-  __TEXT.__oslogstring: 0x1531e
-  __TEXT.__objc_methname: 0x23bd8
-  __TEXT.__cstring: 0x1b6c4
-  __TEXT.__objc_methtype: 0x6a1a
-  __TEXT.__gcc_except_tab: 0x333c
-  __TEXT.__swift5_typeref: 0x19c0
-  __TEXT.__constg_swiftt: 0x1478
-  __TEXT.__swift5_reflstr: 0xc17
-  __TEXT.__swift5_fieldmd: 0x10c0
+  __TEXT.__oslogstring: 0x155eb
+  __TEXT.__objc_methname: 0x23c65
+  __TEXT.__cstring: 0x1b82a
+  __TEXT.__objc_methtype: 0x6a46
+  __TEXT.__gcc_except_tab: 0x3368
+  __TEXT.__swift5_typeref: 0x19e8
+  __TEXT.__constg_swiftt: 0x14b4
+  __TEXT.__swift5_reflstr: 0xc7a
+  __TEXT.__swift5_fieldmd: 0x10f4
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_types: 0x16c
-  __TEXT.__swift5_capture: 0xa1c
+  __TEXT.__swift5_types: 0x170
+  __TEXT.__swift5_capture: 0xa3c
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_proto: 0x1d4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__info_plist: 0x5a8
-  __TEXT.__unwind_info: 0x7668
-  __TEXT.__eh_frame: 0x66d8
-  __DATA_CONST.__auth_got: 0x1748
+  __TEXT.__unwind_info: 0x7688
+  __TEXT.__eh_frame: 0x66b8
+  __DATA_CONST.__auth_got: 0x1760
   __DATA_CONST.__got: 0x1ae0
-  __DATA_CONST.__auth_ptr: 0x688
-  __DATA_CONST.__const: 0x11f08
-  __DATA_CONST.__cfstring: 0xce60
-  __DATA_CONST.__objc_classlist: 0x920
+  __DATA_CONST.__auth_ptr: 0x698
+  __DATA_CONST.__const: 0x12078
+  __DATA_CONST.__cfstring: 0xce80
+  __DATA_CONST.__objc_classlist: 0x928
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x478
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_arrayobj: 0x1b0
-  __DATA.__objc_const: 0x24030
-  __DATA.__objc_selrefs: 0x81f0
-  __DATA.__objc_ivar: 0x804
-  __DATA.__objc_data: 0x6748
-  __DATA.__data: 0x4b18
+  __DATA.__objc_const: 0x24110
+  __DATA.__objc_selrefs: 0x8208
+  __DATA.__objc_ivar: 0x808
+  __DATA.__objc_data: 0x6818
+  __DATA.__data: 0x4af8
   __DATA.__bss: 0x3b08
-  __DATA.__common: 0x194
+  __DATA.__common: 0xe4
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9867
-  Symbols:   1794
-  CStrings:  10880
+  Functions: 9885
+  Symbols:   1800
+  CStrings:  10906
 
Symbols:
+ _$ss20__StaticArrayStorageCN
+ _$ss5Int32VMn
+ __swiftImmortalRefCount
+ _notify_cancel
+ _notify_get_state
+ _notify_is_valid_token
+ _notify_register_dispatch
- _$sSS1poiyS2S_SStFZ
CStrings:
+ "\x01\x11!\x1a\x12"
+ "@\"_TtC14GameDaemonCore18GKGameModeListener\""
+ "GKGameModeListener: Deallocating"
+ "GKGameModeListener: Failed to register for game mode changed notification, status: %!u(MISSING)"
+ "GKGameModeListener: Game Mode Status is now %!l(MISSING)ld, calling game mode changed handler with isActive=%!{(MISSING)bool}d"
+ "GKGameModeListener: Initializing"
+ "GKGameModeListener: Invalid game mode changed notify token"
+ "GKGameModeListener: Received game mode changed notification"
+ "GKGameModeListener: Received game mode changed notification after event stream was deallocated name"
+ "GKGameModeListener: notify_get_state() failed with error %!u(MISSING)"
+ "Game Mode Listener: Game Mode became deactivated, attempting widget refresh"
+ "Game Mode deactivated"
+ "GameDaemonCore.GKGameModeListener"
+ "Setting up Game Mode listener"
+ "T@\"_TtC14GameDaemonCore18GKGameModeListener\",&,N,V_gameModeListener"
+ "_TtC14GameDaemonCore18GKGameModeListener"
+ "_gameModeListener"
+ "com.apple.GameKit.consoleModeChangedQueue"
+ "com.apple.system.console_mode_changed"
+ "gameModeChangedHandler"
+ "gameModeListener"
+ "gameModeNotificationQueue"
+ "gameModeNotificationToken"
+ "initWithHandler:"
+ "setGameModeListener:"
+ "setupGameModeListener"
- "\x01\x11!\x19\x12"

```
