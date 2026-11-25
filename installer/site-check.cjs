const {chromium} = require('playwright-core');
(async () => {
  const browser = await chromium.launch({channel:'chrome',headless:true});
  try {
    const page = await browser.newPage();
    const response = await page.goto('https://pullbrowser.pages.dev/',{waitUntil:'domcontentloaded'});
    if (!response.ok()) throw Error('Website returned '+response.status());
    const expected='https://github.com/Rikix123/pull-updates/releases/download/v7.0.0/Pull-Browser-Setup-7.0.0.exe';
    const links=page.locator('a').filter({hasText:/download for windows|get pull|download pull|download now|download installer|download setup/i});
    try {
      await page.waitForFunction(target => {
        const buttons=[...document.querySelectorAll('a[data-download],a')].filter(a => a.matches('[data-download]') || /download for windows|get pull|download pull|download now|download installer|download setup/i.test(a.textContent));
        return buttons.length>0 && buttons.every(a=>a.href===target);
      },expected,{timeout:25000});
    } finally {
      console.log('Live download links:', await links.evaluateAll(nodes=>nodes.map(n=>[n.innerText,n.href])));
      console.log('Site scripts:',await page.locator('script[src]').evaluateAll(nodes=>nodes.map(n=>n.src)));
    }
  } finally { await browser.close(); }
})().catch(e=>{console.error(e);process.exitCode=1});
