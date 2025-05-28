## com.apple.alarm

> `/System/Library/UserEventPlugins/com.apple.alarm.plugin/com.apple.alarm`

```diff

-324.40.2.0.0
+328.100.1.0.0
   __TEXT.__text: 0x2430
   __TEXT.__auth_stubs: 0x480
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x1af
-  __TEXT.__oslogstring: 0x60d
+  __TEXT.__oslogstring: 0x67d
   __TEXT.__unwind_info: 0xb0
   __DATA.__auth_got: 0x240
   __DATA.__got: 0x48
CStrings:
+ "Adding alarm \"%{public}s\""
+ "Alarm event \"%{public}s\" is fired and active."
+ "Firing event \"%{public}s\" which was due %lld sec ago."
+ "Received request to remove alarm \"%{public}s\" with token %llu\n"
+ "Registering job \"%{public}s\" due in %lld seconds."
+ "Removing alarm \"%{public}s\""
+ "Resetting %s job \"%{public}s\", now due in %lld seconds."
+ "Scheduled wake for %.1fs on behalf of \"%{public}s\"."
+ "Setting timer for \"%{public}s\" in %lld seconds."
+ "System woke up due to \"%{public}s\" which was due at: %lld"
+ "Un-firing event \"%{public}s\" which is due in %lld sec."
+ "Unable to schedule wake for %.1fs on behalf of \"%{public}s\", IOPMRequestSysWake() returned %d."
+ "Unsupported alarm (Type: \"%{public}s\", Date: \"%{public}s\")"
- "Adding alarm \"%s\""
- "Alarm event \"%s\" is fired and active."
- "Firing event \"%s\" which was due %lld sec ago."
- "Received request to remove alarm \"%s\" with token %llu\n"
- "Registering job \"%s\" due in %lld seconds."
- "Removing alarm \"%s\""
- "Resetting %s job \"%s\", now due in %lld seconds."
- "Scheduled wake for %.1fs on behalf of \"%s\"."
- "Setting timer for \"%s\" in %lld seconds."
- "System woke up due to \"%s\" which was due at: %lld"
- "Un-firing event \"%s\" which is due in %lld sec."
- "Unable to schedule wake for %.1fs on behalf of \"%s\", IOPMRequestSysWake() returned %d."
- "Unsupported alarm (Type: \"%s\", Date: \"%s\")"

```
