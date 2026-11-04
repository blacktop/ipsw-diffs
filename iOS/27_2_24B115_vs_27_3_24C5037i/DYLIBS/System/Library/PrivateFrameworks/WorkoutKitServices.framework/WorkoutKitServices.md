## WorkoutKitServices

> `/System/Library/PrivateFrameworks/WorkoutKitServices.framework/WorkoutKitServices`

```diff

-2027.1.63.0.0
-  __TEXT.__text: 0x57c8
+2027.2.25.0.0
+  __TEXT.__text: 0x31fc
   __TEXT.__objc_methlist: 0x218
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__const: 0x50
   __TEXT.__cstring: 0x212
-  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__unwind_info: 0x1b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x118
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__got: 0x50
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x148
   __AUTH_CONST.__auth_got: 0x0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 80
-  Symbols:   145
+  Functions: 79
+  Symbols:   157
   CStrings:  17
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x8
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x4
+ _objc_retain_x8
- __WorkoutKitErrorForXPCConnection
- _objc_retainAutoreleasedReturnValue
- _objc_storeStrong
Functions:
~ +[WorkoutKitXPCServiceHelper sharedInstance] : 60 -> 40
~ -[WorkoutKitXPCServiceHelper _init] : 152 -> 56
~ -[WorkoutKitXPCServiceHelper presentWorkoutCompositionData:completion:] : 504 -> 308
~ ___71-[WorkoutKitXPCServiceHelper presentWorkoutCompositionData:completion:]_block_invoke : 336 -> 188
~ ___71-[WorkoutKitXPCServiceHelper presentWorkoutCompositionData:completion:]_block_invoke_2 : 160 -> 116
~ ___71-[WorkoutKitXPCServiceHelper presentWorkoutCompositionData:completion:]_block_invoke_3 : 112 -> 24
~ __WorkoutKitConnectWithBlock : 776 -> 500
~ -[WorkoutKitXPCServiceHelper presentWorkoutConfigurationData:completion:] : 136 -> 4
~ -[WorkoutKitXPCServiceHelper openWorkoutAppWithWorkoutPlanData:completion:] : 144 -> 12
~ -[WorkoutKitXPCServiceHelper openWorkoutAppWithWorkoutPlanData:autostartWorkoutPlan:completion:] : 528 -> 316
~ ___96-[WorkoutKitXPCServiceHelper openWorkoutAppWithWorkoutPlanData:autostartWorkoutPlan:completion:]_block_invoke : 352 -> 204
~ ___96-[WorkoutKitXPCServiceHelper openWorkoutAppWithWorkoutPlanData:autostartWorkoutPlan:completion:]_block_invoke_2 : 160 -> 116
~ ___96-[WorkoutKitXPCServiceHelper openWorkoutAppWithWorkoutPlanData:autostartWorkoutPlan:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper openWorkoutAppWithWorkoutCompositionData:completion:] : 504 -> 308
~ ___82-[WorkoutKitXPCServiceHelper openWorkoutAppWithWorkoutCompositionData:completion:]_block_invoke : 336 -> 188
~ ___82-[WorkoutKitXPCServiceHelper openWorkoutAppWithWorkoutCompositionData:completion:]_block_invoke_2 : 160 -> 116
~ ___82-[WorkoutKitXPCServiceHelper openWorkoutAppWithWorkoutCompositionData:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper openWorkoutAppWithMirroredStartData:completion:] : 504 -> 308
~ ___77-[WorkoutKitXPCServiceHelper openWorkoutAppWithMirroredStartData:completion:]_block_invoke : 336 -> 188
~ ___77-[WorkoutKitXPCServiceHelper openWorkoutAppWithMirroredStartData:completion:]_block_invoke_2 : 160 -> 116
~ ___77-[WorkoutKitXPCServiceHelper openWorkoutAppWithMirroredStartData:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper openWorkoutAppWithActivityType:autostart:completion:] : 444 -> 288
~ ___82-[WorkoutKitXPCServiceHelper openWorkoutAppWithActivityType:autostart:completion:]_block_invoke : 352 -> 204
~ ___82-[WorkoutKitXPCServiceHelper openWorkoutAppWithActivityType:autostart:completion:]_block_invoke_2 : 180 -> 128
~ ___82-[WorkoutKitXPCServiceHelper openWorkoutAppWithActivityType:autostart:completion:]_block_invoke_3 : 108 -> 24
~ -[WorkoutKitXPCServiceHelper endActiveWorkoutPlanWithIdentifier:completion:] : 504 -> 308
~ ___76-[WorkoutKitXPCServiceHelper endActiveWorkoutPlanWithIdentifier:completion:]_block_invoke : 336 -> 188
~ ___76-[WorkoutKitXPCServiceHelper endActiveWorkoutPlanWithIdentifier:completion:]_block_invoke_2 : 160 -> 116
~ ___76-[WorkoutKitXPCServiceHelper endActiveWorkoutPlanWithIdentifier:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper saveWorkoutCompositionData:completion:] : 504 -> 308
~ ___68-[WorkoutKitXPCServiceHelper saveWorkoutCompositionData:completion:]_block_invoke : 336 -> 188
~ ___68-[WorkoutKitXPCServiceHelper saveWorkoutCompositionData:completion:]_block_invoke_2 : 160 -> 116
~ ___68-[WorkoutKitXPCServiceHelper saveWorkoutCompositionData:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper addScheduledWorkouts:sourceBundleId:completion:] : 584 -> 348
~ ___77-[WorkoutKitXPCServiceHelper addScheduledWorkouts:sourceBundleId:completion:]_block_invoke : 348 -> 204
~ ___77-[WorkoutKitXPCServiceHelper addScheduledWorkouts:sourceBundleId:completion:]_block_invoke_2 : 160 -> 116
~ ___77-[WorkoutKitXPCServiceHelper addScheduledWorkouts:sourceBundleId:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper removeScheduledWorkouts:sourceBundleId:completion:] : 584 -> 348
~ ___80-[WorkoutKitXPCServiceHelper removeScheduledWorkouts:sourceBundleId:completion:]_block_invoke : 348 -> 204
~ ___80-[WorkoutKitXPCServiceHelper removeScheduledWorkouts:sourceBundleId:completion:]_block_invoke_2 : 160 -> 116
~ ___80-[WorkoutKitXPCServiceHelper removeScheduledWorkouts:sourceBundleId:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper storeScheduledWorkoutCompositions:sourceBundleId:completion:] : 584 -> 348
~ ___90-[WorkoutKitXPCServiceHelper storeScheduledWorkoutCompositions:sourceBundleId:completion:]_block_invoke : 348 -> 204
~ ___90-[WorkoutKitXPCServiceHelper storeScheduledWorkoutCompositions:sourceBundleId:completion:]_block_invoke_2 : 160 -> 116
~ ___90-[WorkoutKitXPCServiceHelper storeScheduledWorkoutCompositions:sourceBundleId:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper retrieveScheduledWorkoutCompositionsForSourceBundleId:completion:] : 520 -> 308
~ ___95-[WorkoutKitXPCServiceHelper retrieveScheduledWorkoutCompositionsForSourceBundleId:completion:]_block_invoke : 336 -> 188
~ ___95-[WorkoutKitXPCServiceHelper retrieveScheduledWorkoutCompositionsForSourceBundleId:completion:]_block_invoke_2 : 180 -> 128
~ ___95-[WorkoutKitXPCServiceHelper retrieveScheduledWorkoutCompositionsForSourceBundleId:completion:]_block_invoke_3 : 108 -> 24
~ -[WorkoutKitXPCServiceHelper deleteScheduledWorkoutCompositionsForSourceBundleId:completion:] : 520 -> 308
~ ___93-[WorkoutKitXPCServiceHelper deleteScheduledWorkoutCompositionsForSourceBundleId:completion:]_block_invoke : 336 -> 188
~ ___93-[WorkoutKitXPCServiceHelper deleteScheduledWorkoutCompositionsForSourceBundleId:completion:]_block_invoke_2 : 160 -> 116
~ ___93-[WorkoutKitXPCServiceHelper deleteScheduledWorkoutCompositionsForSourceBundleId:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper retrieveWorkoutCompositionFromWorkout:completion:] : 504 -> 308
~ ___79-[WorkoutKitXPCServiceHelper retrieveWorkoutCompositionFromWorkout:completion:]_block_invoke : 336 -> 188
~ ___79-[WorkoutKitXPCServiceHelper retrieveWorkoutCompositionFromWorkout:completion:]_block_invoke_2 : 180 -> 128
~ ___79-[WorkoutKitXPCServiceHelper retrieveWorkoutCompositionFromWorkout:completion:]_block_invoke_3 : 108 -> 24
~ -[WorkoutKitXPCServiceHelper retrieveWorkoutCompositionFromWorkoutUUID:completion:] : 504 -> 308
~ ___83-[WorkoutKitXPCServiceHelper retrieveWorkoutCompositionFromWorkoutUUID:completion:]_block_invoke : 336 -> 188
~ ___83-[WorkoutKitXPCServiceHelper retrieveWorkoutCompositionFromWorkoutUUID:completion:]_block_invoke_2 : 180 -> 128
~ ___83-[WorkoutKitXPCServiceHelper retrieveWorkoutCompositionFromWorkoutUUID:completion:]_block_invoke_3 : 108 -> 24
~ -[WorkoutKitXPCServiceHelper retrieveAuthorizationStateForBundleId:completion:] : 504 -> 308
~ ___79-[WorkoutKitXPCServiceHelper retrieveAuthorizationStateForBundleId:completion:]_block_invoke : 336 -> 188
~ ___79-[WorkoutKitXPCServiceHelper retrieveAuthorizationStateForBundleId:completion:]_block_invoke_2 : 180 -> 128
~ ___79-[WorkoutKitXPCServiceHelper retrieveAuthorizationStateForBundleId:completion:]_block_invoke_3 : 108 -> 24
~ -[WorkoutKitXPCServiceHelper requestAuthorizationForBundleId:completion:] : 504 -> 308
~ ___73-[WorkoutKitXPCServiceHelper requestAuthorizationForBundleId:completion:]_block_invoke : 336 -> 188
~ ___73-[WorkoutKitXPCServiceHelper requestAuthorizationForBundleId:completion:]_block_invoke_2 : 180 -> 128
~ ___73-[WorkoutKitXPCServiceHelper requestAuthorizationForBundleId:completion:]_block_invoke_3 : 108 -> 24
~ -[WorkoutKitXPCServiceHelper setAuthorizationState:forBundleId:completion:] : 584 -> 348
~ ___75-[WorkoutKitXPCServiceHelper setAuthorizationState:forBundleId:completion:]_block_invoke : 348 -> 204
~ ___75-[WorkoutKitXPCServiceHelper setAuthorizationState:forBundleId:completion:]_block_invoke_2 : 160 -> 116
~ ___75-[WorkoutKitXPCServiceHelper setAuthorizationState:forBundleId:completion:]_block_invoke_3 : 112 -> 24
~ -[WorkoutKitXPCServiceHelper handleUninstalledAppIds:completion:] : 504 -> 308
~ ___65-[WorkoutKitXPCServiceHelper handleUninstalledAppIds:completion:]_block_invoke : 336 -> 188
~ ___65-[WorkoutKitXPCServiceHelper handleUninstalledAppIds:completion:]_block_invoke_2 : 160 -> 116
~ ___65-[WorkoutKitXPCServiceHelper handleUninstalledAppIds:completion:]_block_invoke_3 : 112 -> 24
~ ____WorkoutKitConnectWithBlock_block_invoke : 72 -> 52
~ ____WorkoutKitConnectWithBlock_block_invoke_2 : 132 -> 368
```
