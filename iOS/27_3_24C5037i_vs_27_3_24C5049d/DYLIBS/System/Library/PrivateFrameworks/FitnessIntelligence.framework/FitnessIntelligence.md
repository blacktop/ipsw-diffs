## FitnessIntelligence

> `/System/Library/PrivateFrameworks/FitnessIntelligence.framework/FitnessIntelligence`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`

```diff

-2027.2.12.0.0
-  __TEXT.__text: 0x525808
+2027.2.17.0.0
+  __TEXT.__text: 0x5299c4
   __TEXT.__objc_methlist: 0x33c
-  __TEXT.__const: 0x467d0
-  __TEXT.__cstring: 0x42096
-  __TEXT.__swift5_typeref: 0xf796
+  __TEXT.__const: 0x46810
+  __TEXT.__cstring: 0x42056
+  __TEXT.__swift5_typeref: 0xf7b0
   __TEXT.__swift5_reflstr: 0xea1f
   __TEXT.__swift5_assocty: 0x4c40
-  __TEXT.__constg_swiftt: 0xbd14
-  __TEXT.__swift5_fieldmd: 0xe704
+  __TEXT.__constg_swiftt: 0xbd1c
+  __TEXT.__swift5_fieldmd: 0xe6f8
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_proto: 0x3c70
   __TEXT.__swift5_types: 0x1118
-  __TEXT.__swift5_capture: 0x12e0
+  __TEXT.__swift5_capture: 0x12d0
   __TEXT.__swift5_protos: 0xf8
-  __TEXT.__swift_as_entry: 0x48c
-  __TEXT.__swift_as_ret: 0x3a0
-  __TEXT.__swift_as_cont: 0x858
+  __TEXT.__swift_as_entry: 0x494
+  __TEXT.__swift_as_ret: 0x3a8
+  __TEXT.__swift_as_cont: 0x860
   __TEXT.__oslogstring: 0x1ae7
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__unwind_info: 0x1ad38
-  __TEXT.__eh_frame: 0x2a04c
+  __TEXT.__unwind_info: 0x1ad78
+  __TEXT.__eh_frame: 0x2a174
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ad0
+  __DATA_CONST.__const: 0x1a78
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x1248
-  __AUTH_CONST.__const: 0x22a40
+  __AUTH_CONST.__const: 0x22ad0
   __AUTH_CONST.__objc_const: 0x1cb8
-  __AUTH_CONST.__auth_got: 0x1690
+  __AUTH_CONST.__auth_got: 0x16a0
   __AUTH.__objc_data: 0x700
-  __AUTH.__data: 0xed68
+  __AUTH.__data: 0xed70
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0xcf48
   __DATA.__common: 0x190

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 30217
-  Symbols:   6481
+  Functions: 30224
+  Symbols:   6485
   CStrings:  1507
 
Symbols:
+ _swift_retain_x11
+ _swift_retain_x12
+ _symbolic Shy_____G 9HealthKit37HKWorkoutStrengthTrainingExerciseTypeO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 19FitnessIntelligence31SeymourStrengthPlanProgressFactV
CStrings:
+ "    <moment_instruction>\n    Generate a brief, 2-5 sentence message to start the user's workout.\n\n    Required Elements (Weave these together naturally, DO NOT use a rigid template):\n        - A varied, conversational opening.\n        - Every coaching adjustment the plan lists. Give the duration change for one example exercise; naming an example exercise for a rep, set, or load change is optional.\n        - Only when the facts list a New Exercise, name one or two of them. When none are listed, say nothing about new or upcoming exercises, and never round the list off with a set phrase.\n        - The one celebration the facts offer, if any. Body Focus, the week number, the workout's position in the week, the final workout of the week or plan, the Adjustments and the benefit explanations are context, not celebrations.\n        - A closing sentence that is forward-looking and motivational, transitioning the user into this workout. For example, \"Keep the momentum going!\", \"Let's go!\", \"Let's lift!\", \"You've got this!\" and \"It's go time!\" all meet the bar. \"Line up for your workout\" and \"Start your session\" do not — they are actionable but lack motivation.\n\n    Stay inside what the facts say about the user. Do not state or imply how they feel or will feel: no \"enjoy\", \"you'll love it\", \"feel great\", \"that will feel good\". Do not ask the user to try harder. Do not imply an exercise is unfamiliar — a New Exercise is new to this plan, not necessarily to the user, so never write \"your first Chest Press\", \"try Chest Press\" or \"new to you\".\n\n    Say only what the facts state. If neither an adjustment nor a hold-week benefit is listed, write nothing about adjustments — do not announce that the workout is unchanged or that nothing is new, because those are claims in their own right and the facts do not support them. A hold week is different: when the facts give a hold-week benefit, saying the weights stay the same is the point of the note.\n\n    Claim only the coverage the facts state. When a fact says all of your reps increased, do not widen that to every exercise — a workout can mix rep-based and timed moves, so \"all of your reps are going up\" is true where \"reps are up for all your exercises\" is not. Take every count from the \"Workout Number:\" line exactly as written — never compute a count, total, fraction or share of the week from it.\n\n    Example flows, quoted from the specification's approved notes. Copy the SHAPE and the\n    register, never the wording — reusing these sentences verbatim is a failure, and the\n    closing line especially must be freshly written for the user in front of you.\n\n    - \"Welcome to your plan! Your moves this week include Incline Chest Press with a barbell and Halo with a kettlebell. Any of the estimated weights can be changed if another weight works better for you.\"\n    - \"Your recommended weights are heavier than last week as you continue to progress. Get ready for Biceps Curl with dumbbells at 15 pounds. Lifting heavier is how you can continue to get stronger.\"\n    - \"You got in all your workouts so far this week. Finish today's and your first week is complete! Keep the momentum going!\"\n\n    </moment_instruction>\n\n    <plan_information>\n    "
+ "Adding more volume over time is great for keeping your progress on track."
+ "More time in each move means more opportunity for your muscles to grow and get stronger."
+ "allTimeDuration"
+ "allTimeWeight"
+ "invalidateSnapshotRetriever()"
- "    <moment_instruction>\n    Generate a brief, 2-5 sentence message to start the user's workout.\n\n    Required Elements (Weave these together naturally, DO NOT use a rigid template):\n        - A varied, conversational opening.\n        - Every coaching adjustment the plan lists. Give the amount for a duration change; naming an example exercise for a rep, set, or load change is optional.\n        - Only when the facts list a New Exercise, name one or two of them. When none are listed, say nothing about new or upcoming exercises, and never round the list off with a set phrase.\n        - The one celebration the facts offer, if any. Body Focus, the week number, the workout's position in the week, the final workout of the week or plan, the Adjustments and the benefit explanations are context, not celebrations.\n        - A closing sentence that is forward-looking and motivational, transitioning the user into this workout. \"Keep the momentum going!\", \"Let's go!\", \"Let's lift!\", \"You've got this!\" and \"It's go time!\" all meet the bar. \"Line up for your workout\" and \"Start your session\" do not — they are actionable but lack motivation.\n\n    Stay inside what the facts say about the user. Do not state or imply how they feel or will feel: no \"enjoy\", \"you'll love it\", \"feel great\", \"that will feel good\". Do not ask the user to try harder. Do not imply an exercise is unfamiliar — a New Exercise is new to this plan, not necessarily to the user, so never write \"your first Chest Press\", \"try Chest Press\" or \"new to you\".\n\n    Say only what the facts state. If neither an adjustment nor a hold-week benefit is listed, write nothing about adjustments — do not announce that the workout is unchanged or that nothing is new, because those are claims in their own right and the facts do not support them. A hold week is different: when the facts give a hold-week benefit, saying the weights stay the same is the point of the note.\n\n    Claim only the coverage the facts state. When a fact says all of your reps increased, do not widen that to every exercise — a workout can mix rep-based and timed moves, so \"all of your reps are going up\" is true where \"reps are up for all your exercises\" is not. Take every count from the \"Workout Number:\" line exactly as written — never compute a count, total, fraction or share of the week from it.\n\n    Example flows, quoted from the specification's approved notes. Copy the SHAPE and the\n    register, never the wording — reusing these sentences verbatim is a failure, and the\n    closing line especially must be freshly written for the user in front of you.\n\n    - \"Welcome to your plan! Your moves this week include Incline Chest Press with a barbell and Halo with a kettlebell. Any of the estimated weights can be changed if another weight works better for you.\"\n    - \"Your recommended weights are heavier than last week as you continue to progress. Get ready for Biceps Curl with dumbbells at 15 pounds. Lifting heavier is how you can continue to get stronger.\"\n    - \"You got in all your workouts so far this week. Finish today's and your first week is complete! Keep the momentum going!\"\n\n    </moment_instruction>\n\n    <plan_information>\n    "
- "All of your exercise durations increased by <duration_increase_amount>."
- "Some of your exercise durations increased by <duration_increase_amount>."
- "Your body is constantly adapting, and taking on a little more resistance helps keep the strength gains coming."
- "allTimeTotals"
- "duration_increase_amount"
```
