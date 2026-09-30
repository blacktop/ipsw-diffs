## AirPlayReceiver

> `/Applications/AirPlayReceiver.app/AirPlayReceiver`

```diff

-16.4.5.0.0
-  __TEXT.__text: 0x16ab0
-  __TEXT.__auth_stubs: 0x1250
+16.4.7.0.0
+  __TEXT.__text: 0x183cc
+  __TEXT.__auth_stubs: 0x1260
   __TEXT.__objc_methlist: 0x8b4
   __TEXT.__const: 0x10a4
   __TEXT.__cstring: 0xc8f
-  __TEXT.__swift5_typeref: 0xe50
+  __TEXT.__swift5_typeref: 0xe40
   __TEXT.__swift5_fieldmd: 0x44c
   __TEXT.__constg_swiftt: 0xa58
   __TEXT.__objc_methname: 0x1c77
   __TEXT.__swift5_reflstr: 0x555
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__oslogstring: 0xc35
+  __TEXT.__oslogstring: 0xced
   __TEXT.__swift5_assocty: 0x160
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x78

   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x5f8
+  __TEXT.__unwind_info: 0x608
   __TEXT.__eh_frame: 0x328
-  __DATA_CONST.__auth_got: 0x928
+  __DATA_CONST.__auth_got: 0x930
   __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__auth_ptr: 0x538
+  __DATA_CONST.__auth_ptr: 0x540
   __DATA_CONST.__const: 0xcc8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist2: 0x8

   __DATA.__objc_const: 0x1600
   __DATA.__objc_selrefs: 0x6f8
   __DATA.__objc_data: 0x700
-  __DATA.__data: 0x1068
+  __DATA.__data: 0x1078
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0xf8
   __DATA.__bss: 0xf60

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 533
-  Symbols:   549
+  Functions: 539
+  Symbols:   550
   CStrings:  511
 
Symbols:
+ _objc_release_x28
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer
CStrings:
+ "Acquired background runtime assertion: %{public}s"
+ "FATAL: Unable to acquire domain assertion for airplay receiver: %{public}s"
+ "Foreground requested for reason: %{public}s"
+ "Invalidating background runtime assertion: %{public}s, reason: %{public}s"
+ "MirroringPIPCoordinator: Finished transitioning from full screen to PIP for session: %{public}s"
+ "MirroringPIPCoordinator: Source view is yet attached to a window, returning the first window of the application: %{public}@"
+ "MirroringPIPCoordinator: Started transitioning from full screen to PIP for session: %{public}s"
+ "MirroringPIPCoordinator: Transitioning from preview to user interface for session: %{public}s"
+ "MirroringPIPCoordinator: Updating picture and picture with intent to start when application enters background: %{bool,public}d"
+ "MirroringPIPCoordinator: willStopPictureInPicture, preparing full screen view mirroring for reason (%{public}s)"
+ "MirroringPIPViewController: Updating preferred content size on pip controller to new width %{public}f new height %{public}f"
+ "Received device keybag lock notification, device is %{public}s"
+ "Showing [%{public}s] window."
+ "Start receiver server for reason: %{public}s"
+ "Suspending UI for reason: %{public}s"
+ "Unable to foreground ourself due to error: %{public}s"
+ "Unable to show accept dialog due to error: %{public}s"
+ "User %{public}s the request to begin stream."
+ "[%{public}s] openURLContexts"
+ "[%{public}s] sceneDidEnterBackground"
+ "[%{public}s] sceneWillConnect"
+ "[%{public}s] sceneWillEnterForeground"
+ "[%{public}s] sceneWillEnterForeground while in PiP, manually stopping PiP"
+ "cancelPermission with uuid: %{public}s"
+ "didFinishLaunching: options=%{public}s"
+ "shouldAskPermission with uuid: %{public}s fromClient: %{public}s"
- "Acquired background runtime assertion: %s"
- "FATAL: Unable to acquire domain assertion for airplay receiver: %s"
- "Foreground requested for reason: %s"
- "Invalidating background runtime assertion: %s, reason: %s"
- "MirroringPIPCoordinator: Finished transitioning from full screen to PIP for session: %s"
- "MirroringPIPCoordinator: Source view is yet attached to a window, returning the first window of the application: %@"
- "MirroringPIPCoordinator: Started transitioning from full screen to PIP for session: %s"
- "MirroringPIPCoordinator: Transitioning from preview to user interface for session: %s"
- "MirroringPIPCoordinator: Updating picture and picture with intent to start when application enters background: %{bool}d"
- "MirroringPIPCoordinator: willStopPictureInPicture, preparing full screen view mirroring for reason (%s)"
- "MirroringPIPViewController: Updating preferred content size on pip controller to new width %f new height %f"
- "Received device keybag lock notification, device is %s"
- "Showing [%s] window."
- "Start receiver server for reason: %s"
- "Suspending UI for reason: %s"
- "Unable to foreground ourself due to error: %s"
- "Unable to show accept dialog due to error: %s"
- "User %s the request to begin stream."
- "[%s] openURLContexts"
- "[%s] sceneDidEnterBackground"
- "[%s] sceneWillConnect"
- "[%s] sceneWillEnterForeground"
- "[%s] sceneWillEnterForeground while in PiP, manually stopping PiP"
- "cancelPermission with uuid: %s"
- "didFinishLaunching: options=%s"
- "shouldAskPermission with uuid: %s fromClient: %s"

```
