# The Flash

Points: 40

## Description
The new Justice League movies nerfed the Flash, so clam made his [own rendition](https://the-flash.web.actf.co/)! Can you get the flag before the Flash swaps it out at the speed of light?

## Solution

When loading the page, we can see that we're greeted with a paragraph saying:

```html
<p id="flash">actf{this_is_not_the_flag}</p>
```

Reviewing the [source code](./flash.js) and using the browser developer tools Sources tab, I noticed that there was a section where the element above (variable `x`) is updated based on some interval:

```javascript
const x = document['getElementById']//..

setInterval(() => {
    // x[_0x24a935(0xdc, '1WY2')]
}, 0x64);
```

I then noticed that the paragraph `innerText` was actually being modified in short flashes. These flashes were too fast for me to actually see what the paragraph changed into.

I decided to utilize the Chrome developer tools feature to [define a breakpoint when a DOM element changes](https://developer.chrome.com/docs/devtools/javascript/breakpoints/#dom).

In the Elements tab, I right clicked on the `body` tag > Break on > subtree modifications. The next time the `p` element refreshed, the debugger paused execution and the flag was exposed:

```html
<p id="flash">actf{sp33dy_l1ke_th3_fl4sh}</p>
```