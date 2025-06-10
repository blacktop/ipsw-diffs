## com.apple.driver.SecureRTBuddyProxy

> `com.apple.driver.SecureRTBuddyProxy`

```diff

-618.100.37.0.0
-  __TEXT.__cstring: 0xd96
+693.0.0.0.0
+  __TEXT.__cstring: 0x11c7
   __TEXT.__const: 0x88
-  __TEXT_EXEC.__text: 0x9b44
+  __TEXT_EXEC.__text: 0xa434
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8
-  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__auth_got: 0x2c0
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x1030
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: AE584595-413E-3AF6-98CC-27A4D01A75F2
-  Functions: 280
+  UUID: 91FEBDDB-E7A4-3E7B-91D0-79DF14FDB322
+  Functions: 292
   Symbols:   0
-  CStrings:  74
+  CStrings:  82
 
CStrings:
+ "\"%s\" @%s:%d"
+ "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"tb_service_connection_message_configure_reply failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(rtbuddyservice_powerstate__decode(msg, &next) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTBuddyService.PowerState\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(rtbuddyservice_powerstate__decode(msg, &prev) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTBuddyService.PowerState\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(rtbuddyservice_powerstate__decode(msg, &state) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTBuddyService.PowerState\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->activatemapper != ((void*)0)) && \\\"implementation for activateMapper is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->changepowerstateentry != ((void*)0)) && \\\"implementation for changePowerStateEntry is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->changepowerstateexit != ((void*)0)) && \\\"implementation for changePowerStateExit is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->checkforwork != ((void*)0)) && \\\"implementation for checkForWork is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->fetch != ((void*)0)) && \\\"implementation for fetch is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->fetchbase != ((void*)0)) && \\\"implementation for fetchBase is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->fetchexceptions != ((void*)0)) && \\\"implementation for fetchExceptions is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->fetchthread != ((void*)0)) && \\\"implementation for fetchThread is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->notifypowerstatechange != ((void*)0)) && \\\"implementation for notifyPowerStateChange is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->outboxnotemptyinterrupt != ((void*)0)) && \\\"implementation for outboxNotEmptyInterrupt is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->performpowerstatechange != ((void*)0)) && \\\"implementation for performPowerStateChange is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->recordpowerstate != ((void*)0)) && \\\"implementation for recordPowerState is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->start != ((void*)0)) && \\\"implementation for Start is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "12111112122212121111111111112122"
+ "1211111212221212121111111122221111111111"
+ "1211121111111222"
+ "OSBoundedPtr.h"
+ "The offset of the pointer inside its valid memory range can't be represented using int32_t"
+ "The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range"
+ "This bounded_ptr is pointing to memory outside of what can be represented by a native pointer."
+ "bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally"
+ "bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow."
+ "claim-wake-endpoint-flags"
- "\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"tb_service_connection_message_configure_reply failed\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(rtbuddyservice_powerstate__decode(msg, &next) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTBuddyService.PowerState\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(rtbuddyservice_powerstate__decode(msg, &prev) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTBuddyService.PowerState\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(rtbuddyservice_powerstate__decode(msg, &state) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTBuddyService.PowerState\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->activatemapper != NULL) && \\\"implementation for activateMapper is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->changepowerstateentry != NULL) && \\\"implementation for changePowerStateEntry is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->changepowerstateexit != NULL) && \\\"implementation for changePowerStateExit is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->checkforwork != NULL) && \\\"implementation for checkForWork is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->fetch != NULL) && \\\"implementation for fetch is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->fetchbase != NULL) && \\\"implementation for fetchBase is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->fetchexceptions != NULL) && \\\"implementation for fetchExceptions is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->fetchthread != NULL) && \\\"implementation for fetchThread is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->notifypowerstatechange != NULL) && \\\"implementation for notifyPowerStateChange is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->outboxnotemptyinterrupt != NULL) && \\\"implementation for outboxNotEmptyInterrupt is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->performpowerstatechange != NULL) && \\\"implementation for performPowerStateChange is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->recordpowerstate != NULL) && \\\"implementation for recordPowerState is not present\\\"\" @%s:%d"
- "\"TB_ASSERT: \" \"(server->start != NULL) && \\\"implementation for Start is not present\\\"\" @%s:%d"
- "12111112122212121111111111112"
- "121111121222121212111111122221111111111"
- "121112111112"

```
