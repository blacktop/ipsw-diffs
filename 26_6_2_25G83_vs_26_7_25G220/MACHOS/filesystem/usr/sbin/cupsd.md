## cupsd

> `usr/sbin/cupsd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-522.8.0.0.0
-  __TEXT.__text: 0x4314c
+522.9.1.0.0
+  __TEXT.__text: 0x4187c
   __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__cstring: 0x1178f
+  __TEXT.__cstring: 0x11410
   __TEXT.__const: 0x340
   __TEXT.__oslogstring: 0x24
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__unwind_info: 0x568
   __DATA_CONST.__auth_got: 0xf90
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x78

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 413
+  Functions: 404
   Symbols:   532
-  CStrings:  2704
+  CStrings:  2674
 
CStrings:
+ "No valid attributes-charset, defaulting to utf-8."
+ "No valid attributes-natural-language, using default language."
+ "Rejecting cupsPortMonitor value for printer %s, as it contains injected LF and/or CR characters."
- "."
- ".."
- "Added subscription #%d for job %d."
- "Added subscription #%d for printer \"%s\"."
- "Added subscription #%d for server."
- "Bad notify-user-data \"%s\"."
- "Job subscriptions cannot be renewed."
- "Missing notify-subscription-ids attribute."
- "No subscription attributes in request."
- "No subscriptions found."
- "Subscription #%d does not exist."
- "There are too many subscriptions."
- "cancel_subscription(con=%p[%d], sub_id=%d)"
- "copy_subscription_attrs(con=%p, sub=%p, ra=%p, exclude=%p)"
- "copy_subscription_attrs: notify-events"
- "create_subscriptions(con=%p(%d), uri=\"%s\")"
- "create_subscriptions: Limiting notify-lease-duration to %d seconds."
- "get_notifications(con=%p[%d])"
- "get_subscription_attrs(con=%p[%d], sub_id=%d)"
- "get_subscriptions(con=%p[%d], uri=%s)"
- "mailto:"
- "my-subscriptions"
- "notify-events not specified."
- "notify-get-interval"
- "notify-lease-duration=%d"
- "notify-sequence-numbers"
- "notify-subscription-ids"
- "notify-time-interval=%d"
- "pullmethod=\"%s\""
- "recipient=\"%s\""
- "renew_subscription(con=%p[%d], sub_id=%d)"
- "renew_subscription: Limiting notify-lease-duration to %d seconds."
- "sanitize_ipp_text() called with invalid arguments for printer-geo-location"
```
