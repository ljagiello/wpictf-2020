# reversing - danger-Live-and-Malicious-Code

## Challenge
Like the title says, this challenge is dangerous and contains live malware.

Shoutout to the hacker that I stole this from challenge from. Sadly I can't give
them credit because they sent the phish from a compromised email, but it's
literally his/her code. I just defanged it (a little bit - it will still crash
your webbrowser (usually, but don't test that outside of a VM)) and stuck a WPI
flag in here.

To prevent accidental execution the file has been zipped with the password
"I_understand_that_this_challenge_contains_LIVE_MALWARE"

http://us-east-1.linodeobjects.com/wpictf-challenge-files/invoice.zip

made by: The_Abjuri5t (John F.)

## Solution
Modified version on javascript delivered with this challenge:
```javascript
var a = ['ps:', 'cte', '5df', 'se_', 'toS', 'ing', 'tri', 'sub', 'lac', 'ryt', 'd}.', 'cod', 'pro', '_no', 'ran', 'ing', 'dom', 'str', 'ete', 'rep'];

function abc(def) {
}(function(c, d) {
    var e = function(f) {
        while (--f) {
            c['push'](c['shift']());
        }
    };
    e(++d);
}(a, 0xa8));

var b = function(c, d) {
    c = c - 0x0;
    var e = a[c];
    return e;
};
var c = 'htt' + b('0xc') + '//t' + b('0x1') + b('0xe') + 'xc-' + 'rWP' + 'I';
var d = '{Oh' + b('0x5') + b('0xf') + b('0x4') + b('0x3') + b('0x7') + '_d';
var e = b('0xa') + b('0xd') + b('0x2') + 'net' + '/';
var f = Math['random']()['toString'](0x6)['substring'](0x2, 0xf) + Math['random']()['toString'](0x10)['substring'](0x2, 0xf);
var g = Math['random']()['toString'](0x24)['substring'](0x2, 0xf) + Math['random']()['toString'](0x24)['substring'](0x2, 0xf);
console.log(c + d + e + '?' + f + '=' + g);
``` 

```
➜  node solve.js
https://tryt5dfxc-rWPI{Oh_nose_procoding_detected}.net/?2215044032135e50766d7a9e5f=npv6yadn1ve77f33kf56ds
```

## Flag
```
WPI{Oh_nose_procoding_detected}
```
